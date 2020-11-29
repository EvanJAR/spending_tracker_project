import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction("Amazon", "Entertainment", 25, 6)

    def test_transaction_has_tag(self):
        self.assertEqual("Entertainment", self.transaction.tag)
    
    def test_transaction_has_merchant(self):
        self.assertEqual("Amazon", self.transaction.merchant)
    
    def test_transaction_has_amount(self):
        self.assertEqual(25, self.transaction.amount)
    
    def test_transaction_has_id(self):
        self.assertEqual(6, self.transaction.id)
    
    
