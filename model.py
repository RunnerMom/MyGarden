from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, \
Enum, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from datetime import datetime

engine = create_engine('postgresql+psycopg2://alm:password@localhost/developher2', echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit=False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

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


class Order(Base):
	
	__tablename__ = 'orders'

	id = Column(Integer, primary_key = True)
	order_date = Column(DateTime)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	product_id = Column(Integer, ForeignKey(''))
	pickup_date = Column(DateTime)



class Product(Base):

	__tablename__ = 'products'

	id = Column(Integer, primary_key = True)
	category = Column(Enum('apples', 'carrots', 'lettuce', 'squash', 'tomatoes', name='product_types'))
	nametag = Column(String(128), nullable = False)
	quantity = Column(Integer, nullable = False)
	expiration_date = Column(DateTime)
	price = Column(Float, nullable = False)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


