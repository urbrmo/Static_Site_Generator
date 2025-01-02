import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

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


class TestParentNode(unittest.TestCase):

    def test_simple_parent_with_leaves(self):
        parent = ParentNode('p', [
            LeafNode('b', 'Bold text'),
            LeafNode(None, 'Normal text')
        ])
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text</p>")

    def test_nested_parents(self):
        nested_parent = ParentNode('div', [
            ParentNode('p', [
                LeafNode('b', 'Bold text'),
                LeafNode(None, 'Plain text')
            ]),
            LeafNode('i', 'Italic text')
        ])
        self.assertEqual(nested_parent.to_html(), "<div><p><b>Bold text</b>Plain text</p><i>Italic text</i></div>")

    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode('p', None)
            parent.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no children")

    def test_no_tag(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode(None, [])
            parent.to_html()
        self.assertEqual(str(context.exception), "Invalid HTML: no tag")


if __name__ == '__main__':
    unittest.main()