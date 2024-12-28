import unittest

from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()