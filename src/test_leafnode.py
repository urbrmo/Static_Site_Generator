import unittest

from leafnode import LeafNode

class TestleafNode(unittest.TestCase):        
    def test_tag_with_text(self):
        node = LeafNode(tag="p", value="Click here")
        self.assertEqual(node.to_html(), "<p>Click here</p>")

    def test_tag_with_properties(self):
        node = LeafNode("a", "click here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">click here</a>')

    def test_value_none(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None, {"href": "https://example.com"})
            node.to_html()

    def test_tag_none(self):
        node = LeafNode(None, "raw text here")
        self.assertEqual(node.to_html(), "raw text here")