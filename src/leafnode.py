from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def __init_subclass__(cls):
        raise TypeError("LeafNode is final and cannot be subclassed")

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf node has no value")
        if self.tag == None:
            return self.value
        props_html = self.props_to_html()
        encoded = (
            self.value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        )
        if self.tag == "img":
            return f"<{self.tag}{props_html}>"
        return f"<{self.tag}{props_html}>{encoded}</{self.tag}>"
