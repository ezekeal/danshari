from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None or tag is None:
            raise ValueError("LeafNode requires a value and tag")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def __init_subclass__(cls):
        raise TypeError("LeafNode is final and cannot be subclassed")

    def to_html(self):
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
