from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, url, NumberRange



# class AddPetForm(FlaskForm):
    
    
    
#     notes = StringField('Notes', validators=[Optional()])
    
class AddPetForm(FlaskForm):
    
    name = StringField('Pet name', validators=[InputRequired(message='Pet name can not be blank!')])
    
    species = SelectField('Species', choices=[('d', 'dog'), ('c', 'cat'), ('p', 'porcupine')])

    photo_url = StringField('Photo URL', validators=[Optional(), url(message='Must be a valid URL!')])
    age = FloatField('Age', validators=[Optional(), NumberRange(min=0, max=30.0)])
    notes = StringField('Notes')

