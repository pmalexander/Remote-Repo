from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

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
    
class Bid(Base):
    __tablename__ = "bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)

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

luke = User()
luke.username = "lbaker"
luke.password = "cage"

session.add(luke)
session.commit()

axe = Item()
axe.id = 1
axe.name = "Axe"
axe.description = "Huge"
 
session.add(axe)
session.commit()

lantern = Item()
lantern.id = 2
lantern.name = "Lantern"
lantern.description = "Bright"

session.add(lantern)
session.commit()

remote = Item()
remote.id = 3
remote.name = "Remote"
remote.description = "Multipurpose"

session.add(remote)
session.commit()

rope = Item()
rope.id = 4
rope.name = "Rope"
remote.description = "Lengthy"

session.add(rope)
session.commit()

wheelchair = Item()
wheelchair.id = 5
wheelchair.name = "Wheelchair"
wheelchair.description = "Old"

session.add(wheelchair)
session.commit

session.query(User).all()