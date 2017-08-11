from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
jack = User()
jack.username = "jbaker"
jack.password = "chainsaw"

session.add(jack)
session.commit()

marguerite = User()
marguerite.username = "mbaker"
marguerite.password = "bugs"

session.add(marguerite)
session.commit()

mansion = Item()
mansion.id = 1
mansion.name = "Residence"
mansion.description = "Creepy"
mansion.start_time = DateTime 

session.add(mansion)
session.commit()

basement = Item()
basement.id = 2
basement.name = "Storage"
basement.description = "Scary"
basement.start_time = DateTime

session.add(basement)
session.commit()

class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)

session.query(User).all()