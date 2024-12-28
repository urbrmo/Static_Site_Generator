import unittest

from htmlnode import HTMLNode

class Testhtmlnode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click here")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"href": "https://example.com", "target": "_blank"})

if __name__ == '__main__':
    unittest.main()