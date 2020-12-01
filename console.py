from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction

import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

transaction_repository.delete_all()
tag_repository.delete_all()
merchant_repository.delete_all()

tag1 = Tag("Entertainment")
tag_repository.save(tag1)

tag2 = Tag("Transport")
tag_repository.save(tag2)

tag3 = Tag("Food")
tag_repository.save(tag3)

tag4 = Tag("Drink")
tag_repository.save(tag4)



merchant1 = Merchant("Amazon")
merchant_repository.save(merchant1)

merchant2 = Merchant("ScotRail")
merchant_repository.save(merchant2)

merchant3 = Merchant("Tesco")
merchant_repository.save(merchant3)

merchant4 = Merchant("Woolworths")
merchant_repository.save(merchant4)

transaction1 = Transaction(merchant1, tag1, 25)
transaction_repository.save(transaction1)

transaction2 = Transaction(merchant2, tag2, 50)
transaction_repository.save(transaction2)

