from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField

class AddPetForm(FlaskForm):
    
    name = StringField('Pet name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = FloatField('Age')
    notes = StringField('Notes')
    

