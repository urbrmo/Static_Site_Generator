import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_same_properties(self):
        node = TextNode("Hello", TextType.BOLD, "https://boot.dev")
        node2 = TextNode("Hello", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://bootdev.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"

    def test_bold_node_to_html_node(self):
        bold_node = TextNode("Hello, world!", TextType.BOLD)
        html_node = text_node_to_html_node(bold_node)
        assert html_node.tag == "b"
        assert html_node.value == "Hello, world!"

    def test_link_node_to_html_node(self):
        link_node = TextNode("Hello, world!", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(link_node)
        assert html_node.tag == "a"
        assert html_node.value == "Hello, world!"
        assert html_node.props == {"href": "https://example.com"}
    
    def test_image_node_to_html_node(self):
        image_node = TextNode("Hello, world!", TextType.IMAGE, "https://example.com")
        html_node = text_node_to_html_node(image_node)
        assert html_node.tag == "img"
        assert html_node.value == ""
        assert html_node.props == {"src": "https://example.com", "alt":"Hello, world!"}


if __name__ == "__main__":
    unittest.main()