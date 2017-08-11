from tbay import User, Item, Bid, session

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
session.add(mansion)
session.commit()

basement = Item()
basement.id = 2
basement.name = "Storage"
basement.description = "Scary"
session.add(basement)
session.commit()

