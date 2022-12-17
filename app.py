from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddPetForm



app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_BINDS'] = {'testDB' : 'sqlite:///test_pets.db'}


app.debug = True
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


db = SQLAlchemy(app)
app.app_context().push()

migrate = Migrate(app, db)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=1)
    

@app.route('/', methods=['GET', 'POST'])
def main_page():
    pets = Pet.query.all()    
    return render_template('home.html', pets=pets)




@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        pet_to_add = Pet(name=name, 
                         species=species, 
                         photo_url=photo_url, 
                         age=age, 
                         notes=notes)
        
        db.session.add(pet_to_add)
        db.session.commit()        
        
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)
        







# if __name__ == '__main__':
#     app.run(debug=True)