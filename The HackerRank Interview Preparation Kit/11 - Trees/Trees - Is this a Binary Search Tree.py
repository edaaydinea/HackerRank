""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return isBST(root, -1, 10001)

def isBST(root, left, right):
    if root is None:
        return True
    if root.data <= left or root.data>= right:
        return False
    return (isBST(root.left, left, root.data) and isBST(root.right, root.data, right))