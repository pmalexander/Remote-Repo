from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, desc
from sqlalchemy.orm import relationship

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey(user.id, nullable=False)
    
    user_bid = relationship("Bid", backref="bidfor_item")
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    bid = relationship("Bid", uselist=True, backref="User")
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    item_id = Column(Integer, ForeignKey('Item.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    
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
axe.name = "Axe"
axe.description = "Huge"
 
session.add(axe)
session.commit()

lantern = Item()
lantern.name = "Lantern"
lantern.description = "Bright"

session.add(lantern)
session.commit()

remote = Item()
remote.name = "Remote"
remote.description = "Multipurpose"

session.add(remote)
session.commit()

rope = Item()
rope.name = "Rope"
rope.description = "Lengthy"

session.add(rope)
session.commit()

wheelchair = Item()
wheelchair.name = "Wheelchair"
wheelchair.description = "Old"

session.add(wheelchair)
session.commit()

baseball = Item()
baseball.name = "Baseball"
baseball.description = "Round"

session.add(baseball)
session.commit()

jack = session.query(User).filter(User.username == 'Jack').first()
marguerite = session.query(User).filter(User.username == 'Marguerite').first()
luke =session.query(User).filter(User.username == 'Luke').first()

axe = session.query(Item).filter(Item.name == 'Axe').first()
lantern = session.query(Item).filter(Item.name == 'Lantern').first()
remote = session.query(Item).filter(Item.name == 'Remote').first()
rope = session.query(Item).filter(Item.name == 'Remote').first()
wheelchair = session.query(Item).filter(Item.name == 'Wheelchair').first()
baseball = session.query(Item).filter(Item.name == 'Baseball').first()

# Returns a list of all of the user objects
# Note that user objects won't display very prettily by default -
# you'll see their type (User) and their internal identifiers.
session.query(User).all() # Returns a list of all of the user objects

# Returns the first user
session.query(User).first()

# Finds the user with the primary key equal to 1
session.query(User).get(1)

# Returns a list of all of the usernames in ascending order
session.query(User.username).order_by(User.username).all()

# Returns the description of all of the basesballs
session.query(Item.description).filter(Item.name == "baseball").all()

# Return the item id and description for all baseballs which were created in the past.  Remember to import the datetime object: from datetime import datetime
session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()
test = session.query(Item).filter(Item.name == "baseball").first()
session.query(Bid).filter(Item.id == "baseball").order_by(desc(Bid.price))
