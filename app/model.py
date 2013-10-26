from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, \
Enum, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime
import locale

engine = create_engine('postgresql+psycopg2://alm:password@localhost/developher2', echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()



locale.setlocale(locale.LC_ALL, '')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    phone = Column(String(64), nullable=False)
    street_address = Column(String(64), nullable=False)
    city = Column(String(64), nullable=False)
    zip_code = Column(String(15), nullable=False)
    #password = Column(String(64), nullable=False)

    orders = relationship('Order', backref=backref('user'))
    products = relationship('Product', backref=backref('user'))

    # Testing purposes
    def __repr__(self):
        return '<User %r>' % (self.first_name)

class Order(Base):
    
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    pickup_date = Column(DateTime, nullable=False)
    quantity = Column(Integer, nullable=False)
    comments = Column(String(64), nullable=True)
    
    # Testing purposes
    def __repr__(self):
        return '<pickup_date %r>' % (self.pickup_date)

class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    category = Column(Enum('apples', 'carrots', 'lettuce', 'squash', 'tomatoes', name='product_types'))
    nametag = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)
    expiration_date = Column(DateTime)
    unit = Column(Enum('items', 'dozen', 'pounds', name='unit_types'))
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    image_url = Column(String(256), nullable=True)

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
