class GeneralTree:
    def __init__(self, key, child = None):
        self.key = key
        self.child = child
        self.nrbchild = len(child)


class TreeAsBin :
    def __init__(self,key,child = None ,sibling = None):
        self.key = key
        self.child = child
        self.sibling = sibling
