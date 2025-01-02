import unittest

from htmlnode import HTMLNode, LeafNode

class Testhtmlnode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click here")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"href": "https://example.com", "target": "_blank"})

    def test_default_initialization(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')

    def test_repr_method(self):
        node = HTMLNode(tag="div", value="Content", children=[HTMLNode(tag="span")], props={"class": "container"})
        expected_repr = "HTMLNode(div, Content, [HTMLNode(span, None, [], {})], {'class': 'container'})"
        self.assertEqual(repr(node), expected_repr)

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


if __name__ == '__main__':
    unittest.main()