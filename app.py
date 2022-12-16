from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "farts"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogly.db'
app.config['SQLALCHEMY_BINDS'] = {'testDB' : 'sqlite:///test_blogly.db'}


app.debug = True
debug = DebugToolbarExtension(app)
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
    available = db.Column(db.Boolean, nullable=False, default='available')
    j







@app.route('/')
def main_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)