from flask.ext.wtf import Form, validators
from flask.ext.wtf import TextAreaField, FloatField, TextField, HiddenField
from flask.ext.wtf import PasswordField, IntegerField, DateField, SubmitField
from flask.ext.wtf import BooleanField, SelectField, RadioField, SelectMultipleField
import model

class AddProduct(Form):
	category = SelectField('Category', [validators.Required(message=(u'Select a category'))], 
									    choices=[('apples', 'Apples'), 
												('carrots', 'Carrots'), 
												('lettuce', 'Lettuce'), 
												('squash', 'Squash'), 
												('tomatoes', 'Tomatoes')],
										description=u'Category')
	description = TextField('Description', 
					[validators.Required(message=(u'Please add a description of your product'))], 
					description=u'Description')
	quantity = IntegerField('Quantity Available', 
			   		[validators.Required(message=(u'Please indicate how many you have to sell'))],
			   		description='Quantity')
	unit = SelectField('Unit', [validators.Required(message=(u'Select a unit'))], 
						choices=[('items', 'Items'), 
								 ('dozen', 'Dozen'), 
								 ('pounds', 'Pounds')],
						description='Unit')
	expiration_date = DateField('Expiration date', 
					 [validators.Required(message=(u'When does your product need to sell by?'))],
					 description = 'Expiration date')
	price = FloatField('Price per unit', 
		    [validators.Required(message=(u'Please set a unit price for your product'))],
		    description=u'Price')
	image_url = TextField('Link to product image', [validators.Optional()], 
				description=u'Link to product image')


class CreateOrder(Form):
	product_id = IntegerField('Product ID')
	user_id = IntegerField('User ID')
	order_date = DateField('Order date')
	pickup_date = DateField('Pickup date', 
					 [validators.Required(message=(u'When will you pick up your order?'))],
					 description = 'Pickup date')
	quantity = IntegerField('Quantity', 
			   		[validators.Required(message=(u'Please indicate how many you want to buy'))],
			   		description='Quantity')


class Registration(Form):
	user_id = IntegerField('User ID')
	email = TextField('Email Address', 
		    [validators.Email(message=(u"Looks like your email address is invalid.")),
		    validators.Required(message=(u'Please enter your email address.'))],
		    description='Email address')
	phone = TextField('Phone Number', 
		    [validators.Required(message=(u'Please enter your email address.'))],
		    description='Phone number')
	first_name = TextField('First Name',
				 [validators.Required(message=(u'Please enter your first name'))],
		    	 description='First name')
	last_name =  first_name = TextField('Last Name',
				 [validators.Required(message=(u'Please enter your last name'))],
		    	 description='Last name')
	street_address = TextField('Street Address',
				 [validators.Required(message=(u'Please enter your street address'))],
		    	 description='Street address')
	city = TextField('City',
		   [validators.Required(message=(u'Please enter your street address'))],
		   description='City')
	zip_code = TextField('Zip Code',
		   [validators.Required(message=(u'Please enter your zip code'))],
		   description='Zip code')

