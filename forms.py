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
	product_id = HiddenField('Product ID')
	user_id = HiddenField('User ID')
	order_date = HiddenField('Order date')
	expiration_date = DateField('Pickup date', 
					 [validators.Required(message=(u'When will you pick up your order?'))],
					 description = 'Pickup date')
	quantity = IntegerField('Quantity', 
			   		[validators.Required(message=(u'Please indicate how many you want to buy'))],
			   		description='Quantity')


