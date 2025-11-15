class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        str = ""
        if self.props != None:
            for k, v in self.props.items():
                str += f' {k}="{v}"'
        return str

    def __repr__(self):
        str = ""
        str += f"tag: {self.tag}"
        str += f" value: {self.value}"
        str += f" children: {self.children}"
        str += f" props: {self.props}"
        return str
