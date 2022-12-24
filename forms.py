from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, RadioField, BooleanField
from wtforms.validators import InputRequired, Optional, url, NumberRange



# class AddPetForm(FlaskForm):
    

    
class AddPetForm(FlaskForm):
    
    name = StringField('Pet name', validators=[InputRequired(message='Pet name can not be blank!')])
    
    species = SelectField('Species', choices=[('dog', 'dog'), ('cat', 'cat'), ('porcupine', 'porcupine')])

    photo_url = StringField('Photo URL', validators=[Optional(), url(message='Must be a valid URL!')])
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30.0)])
    notes = StringField('Notes')
    available = RadioField('Is this pet available?', choices=[('Available', 'This pet is available'), ('Not Available', 'This pet is not available')])
    

class EditPetForm(FlaskForm):
    
    # DEFAULT = 'https://cdn.vox-cdn.com/thumbor/-famZFxgMFo2h1HQ5UjIIcBszrI=/0x0:1920x1080/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/53254027/who_pokemon.0.jpg'
    photo_url = StringField('Photo URL', validators=[Optional(), url(message='Must be a valid URL!')])
    notes = StringField('Notes', validators=[Optional()])
    available = RadioField('Is this pet available?', choices=[('Available', 'This pet is available'), ('Not Available', 'This pet is not available')])