from TreeBase import *
root = setUpTree()
def delete(root,node):
    if node.left == None or node.right == None:
        if node.parent == None:
            root =  node.left if node.right == None else node.right
        if node.parent.left == node:
            node.parent.left = node.left if node.right == None else node.right
            if node.right != None:
                node.right.parent = node.parent
            if node.left != None:
                node.left.parent = node.parent
        if node.parent.right == node:
            node.parent.right = node.left if node.right == None else node.right
            if node.right != None:
                node.right.parent = node.parent
            if node.left != None:
                node.left.parent = node.parent
    else:
        minNode = findMin(node.right)
        node.key = minNode.key
        node.value = minNode.value
        delete(root,minNode)
def inOrderShow(root):
    if root.left != None:
        inOrderShow(root.left)
    print(root.value)
    if root.right != None:
        inOrderShow(root.right)
inOrderShow(root)
delete(root,search(root,3))
print('*'*20)
inOrderShow(root)
# to make the binary search tree keep efficient, we can randomly generate it to avoid add item in order of increasing or decreasing.
