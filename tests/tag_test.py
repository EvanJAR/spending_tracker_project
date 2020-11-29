import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):
        self.tag = Tag("Entertainment", 7)

    def test_tag_has_category(self):
        self.assertEqual("Entertainment", self.tag.category)

    def test_tag_has_id(self):
        self.assertEqual(7, self.tag.id)