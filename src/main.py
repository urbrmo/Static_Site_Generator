from textnode import TextNode, TextType

def main():
    dummy = TextNode("this is the text", TextType.ITALIC, "https://example.com")
    print(dummy)

main()