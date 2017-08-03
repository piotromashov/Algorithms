#https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    return checkBSTaux(root, float("-infinity"), float("infinity"))
    
    


def checkBSTaux(root, minimum, maximum):
    if(not root.left and not root.right):
        return True
      
    if root.left:
        rightValid = root.left.data < root.data and root.left.data > minimum and checkBSTaux(root.left, minimum, root.data)
    if root.right:
        leftValid = root.right.data > root.data and root.right.data < maximum and checkBSTaux(root.right, root.data, maximum)

    return rightValid and leftValid