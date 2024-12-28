class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        HTML_attributes = ""
        for prop in self.props:
            HTML_attributes += f" {prop}"+ "=" + f'"{self.props[prop]}"'
        return HTML_attributes

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"