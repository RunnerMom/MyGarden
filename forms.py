from flask.ext.wtf import Form, validators
from flask.ext.wtf import TextAreaField, FloatField, TextField
from flask.ext.wtf import PasswordField, IntegerField, DateField, SubmitField
from flask.ext.wtf import BooleanField, SelectField, RadioField, SelectMultipleField
import model

class AddProduct(Form):
	category = SelectField('Category', [validators.Required(message=(u'Select a category'))], 
									  choices=[('apples', 'Apples'), 
												('carrots', 'Carrots'), 
												('lettuce', 'Lettuce'), 
												('squash', 'Squash'), 
												('tomatoes', 'Tomatoes')])
	description = TextField('Description', )

# class EditProfileForm(Form):
#         firstname = TextField('First Name', [validators.Optional()], 
#                                                   description=u'First Name')
#         lastname = TextField('Last Name',[validators.Optional()], 
#                                                  description=u'Last Name')
#         address= TextField('Address',[validators.Optional()], 
#                                            description=u'Address')
#         city= TextField('City',[validators.Optional()], description=u'City')
#         state = TextField('State', [validators.length(max=2), 
#                                                                 validators.Optional()], description=u'State')
#         zipcode = TextField('Zipcode', [validators.Optional()], description=u'Zipcode')
#         country = TextField('Country',[validators.Optional()], description=u'Country')
#         user_disabled= BooleanField('Taking a break? Disable Account')
#         about_me= TextAreaField('About Me', [validators.length(min=0, max=140)],
#                                                 description=u'About Me!!')