from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=[])

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is None:
            return f"{self.value}"
        else:
            if self.props is None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    