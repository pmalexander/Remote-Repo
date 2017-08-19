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
    
    bidded_item = relationship("Bid", backref="bidded_item")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

#sets relationship with the items and the users as bidders for items    
    auc_item = relationship("Item", backref="auc_item")
    auc_bid = relationship("Bid", backref="auc_bidder")
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    item_id = Column(Integer, ForeignKey('Item.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)

Base.metadata.create_all(engine)

#sets usernames and passwords for each bidder
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

#sets the items, names, and descriptions
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
wheelchair = session.query(Item.filter(Item.name == 'Wheelchair').first()
baseball = session.query(Item).filter(Item.name == 'Baseball').first()

all_bids = session.query(Bid).all()

#identifies Jack Baker as the owner of the baseball
baseball = Item(baseball.name="baseball", baseball.description="Round", baseball.owner=jack)
session.add(baseball)
session.commit()
print("{} auctions for {} on {}".format(baseball.owner.username, baseball.name, baseball.start_time))

#identifies both Marguerite and Luke Baker as bidders for the baseball
m_bid = Bid(price = 100, item_id=baseball.id, auc_bidder=marguerite)
l_bid = Bid(price = 200, item_id=baseball.id, auc_bidder=luke)

for bid in all_bids
    item = session.query(Item).filter(Item.id == bid.item_id).first()
    ouruser = session.query(User).filter(User.id == bid._bidder_id).first()
    print("price:{}, bidder:{}, item:{}".format(bid.price, user.name, item.name))

# returns the item_id and description for all baseballs which were created in the past.  
# import the datetime object: from datetime import datetime
session.query(Item.id, Item.description).filter(Item.name == "baseball", Item.start_time < datetime.utcnow()).all()
test = session.query(Item).filter(Item.name == "baseball").first()
session.query(Bid).filter(Item.id == "baseball").order_by(desc(Bid.price))

# Returns the description of all of the basesball
#session.query(Item.description).filter(Item.name == "baseball").all()

# Returns a list of all of the user objects
# Note that user objects won't display very prettily by default -
# you'll see their type (User) and their internal identifiers.
#session.query(User).all() # Returns a list of all of the user objects

# Returns the first user
#session.query(User).first()

# Finds the user with the primary key equal to 1
#session.query(User).get(1)

# Returns a list of all of the usernames in ascending order
# session.query(User.username).order_by(User.username).all()