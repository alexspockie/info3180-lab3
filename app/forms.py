from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
#from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired, Email, Optional

class ContactForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email= StringField('Email',validators=[DataRequired(), Email()])
    subject= StringField('Subject',validators=[DataRequired()])
    message= TextAreaField('Message',validators=[DataRequired()])

    #protect using CSRF TOKEN
    #form should have text field for name,email and subject
    #text area for message