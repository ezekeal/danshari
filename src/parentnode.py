from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is None or tag is None:
            raise ValueError("ParentNode requires a value and tag")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode requires a tag")
        if self.children is None:
            raise ValueError("ParentNode requires children")
        props_html = self.props_to_html()
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}{props_html}>{children_str}</{self.tag}>"
