#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Donor: ')
    bloodtype = StringField('Blood type: ')
    submit = SubmitField('Add Donor')


class DelForm(FlaskForm):
    id = IntegerField('Id number of requeted blood bag:')
    name= StringField('Name of the Recepient:')
    submit = SubmitField('Issue')
