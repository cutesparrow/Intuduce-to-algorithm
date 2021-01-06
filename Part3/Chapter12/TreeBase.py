#binary search tree
class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent


def addOneNode(root, newNode):
    if newNode.key > root.key:
        if root.right == None:
            root.right = newNode
            newNode.parent = root
        else:
            addOneNode(root.right, newNode)
    else:
        if root.left == None:
            root.left = newNode
            newNode.parent = root
        else:
            addOneNode(root.left, newNode)


def search(root, key):
    if root == None or key == root.key:
        return root
    if root.key < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


def findMin(root):
    while root.left != None:
        root = root.left
    return root


def findMax(root):
    while root.right != None:
        root = root.right
    return root


def successor(node):
    if node.right != None:
        return findMin(node.right)
    parent = node.parent
    while parent != None and parent.right == node:
        node = parent
        parent = node.parent
    return parent


def predecessor(node):
    if node.left != None:
        return findMax(node.left)
    parent = node.parent
    while parent != None and parent.left == node:
        node = parent
        parent = node.parent
    return parent


def setUpTree():
    Node15 = Node(15, value="15")
    Node6 = Node(6, value="6")
    Node18 = Node(18, value="18")
    Node3 = Node(3, value="3")
    Node7 = Node(7, value="7")
    Node17 = Node(17, value="17")
    Node20 = Node(20, value="20")
    Node2 = Node(2, value="2")
    Node4 = Node(4, value="4")
    Node13 = Node(13, value="13")
    Node9 = Node(9, value="9")
    addOneNode(Node15, Node6)
    addOneNode(Node15, Node18)
    addOneNode(Node15, Node3)
    addOneNode(Node15, Node7)
    addOneNode(Node15, Node17)
    addOneNode(Node15, Node20)
    addOneNode(Node15, Node2)
    addOneNode(Node15, Node4)
    addOneNode(Node15, Node13)
    addOneNode(Node15, Node9)
    return Node15


def test1():
    root = setUpTree()
    print(findMax(root).value)
    print(findMin(root).value)
    print(successor(root).value)
    print(predecessor(root).value)
    print(successor(search(root, 4)).value)
    print(predecessor(search(root, 17)).value)
