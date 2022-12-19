from flask import Flask, request, render_template, redirect, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddPetForm, EditPetForm



app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
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
    
    DEFAULT = 'https://cdn.vox-cdn.com/thumbor/-famZFxgMFo2h1HQ5UjIIcBszrI=/0x0:1920x1080/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/53254027/who_pokemon.0.jpg'
    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT)
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
        if not photo_url:
            photo_url = Pet.DEFAULT
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
        
@app.route('/pet_id_<int:pet_id>')
def show_pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    
    return render_template('show_pet.html', pet=pet)
    
@app.route('/edit_pet_<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.add(pet)
        db.session.commit()
        
        return redirect('/')
    else:
        return render_template('edit_pet.html', pet=pet, form=form)
    
@app.route('/delete_pet_<int:pet_id>')
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    
    db.session.delete(pet)
    db.session.commit()
    return redirect('/')
    






# if __name__ == '__main__':
#     app.run(debug=True)