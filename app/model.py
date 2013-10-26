from app import db 
import locale

locale.setlocale(locale.LC_ALL, '')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), nullable=False)
    street_address = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    zip_code = db.Column(db.String(15), nullable=False)
    #password = Column(String(64), nullable=False)

    orders = db.relationship('Order', backref='user')
    products = db.relationship('Product', backref='user')

    # Testing purposes
    def __repr__(self):
        return '<User %r>' % (self.first_name)

class Order(db.Model):
    
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    pickup_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(64), nullable=True)
    
    # Testing purposes
    def __repr__(self):
        return '<pickup_date %r>' % (self.pickup_date)

class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.Enum('apples', 'carrots', 'lettuce', 'squash', 'tomatoes', name='product_types'))
    nametag = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    expiration_date = db.Column(db.DateTime)
    unit = db.Column(db.Enum('items', 'dozen', 'pounds', name='unit_types'))
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    image_url = db.Column(db.String(256), nullable=True)

    def show_price(self):
        return locale.currency(self.price)

    def decrease_quantity(self, amount):
        self.quantity -= amount

    # Testing purposes
    def __repr__(self):
        return '<nametag %r>' % (self.nametag)


#Test User
user = {'firstname': 'Crystal', 
        'lastname': 'James',
        'email': 'crystalynn@yahoo.com',
        'phone': '+19176916498',
        'address': '206 West 112th St',
        'city': 'Los Angeles',
        'state': 'CA',
        'zip_code': '90061'}

#Test Buyers
buyers = [{'firstname': 'Isiah', 
            'lastname': 'Richards',
            'email': 'isiah@yahoo.com',
            'phone': '+19176916498',
            'address': '101 Broadway St', 
            'city': 'Los Angeles',
            'state': 'CA',
            'zip_code': '90061'},

            {'firstname': 'Courtney', 
            'lastname': 'Oliva',
            'email': 'courtney@yahoo.com',
            'phone': '+1917691649C8',
            'address': '1056 Main Street',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip_code': '90061'},

            {'firstname': 'JoAnn', 
            'lastname': 'Walker',
            'email': 'joann@yahoo.com',
            'phone': '+19176916498',
            'address': '218 W. 112th Street',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip_code': '90061'},

            {'firstname': 'Aimee', 
            'lastname': 'Morgan',
            'email': 'aimee@yahoo.com',
            'phone': '+19176916498',
            'address': '1512 Crenshaw Blvd',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip_code': '90061'},

            {'firstname': 'Morgan', 
            'lastname': 'Griggs',
            'email': 'morgan@yahoo.com',
            'phone': '+19176916498',
            'address': '1220 Crenshaw Blvd',
            'city': 'Los Angeles',
            'state': 'CA',
            'zip_code': '90061'}]
