#大顶堆
#完全二叉树
class MyHeap:
    def __init__(self,nums):
        self._list = nums
    def getParent(self,i):
        return self._list[int((i+1)/2)-1]
    def getLeft(self,i):
        return self._list[(i+1)*2-1]
    def getRight(self,i):
        return self._list[(i+1)*2]
heap = MyHeap([16,14,10,8,7,9,3,2,4,1])
#print(heap.getParent(heap._list.index(14)))
#print(heap.getLeft(1))
#print(heap.getRight(1))

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def addLeft(self,leftNode):
        if self.left == None and leftNode.value < self.value:
            self.left = leftNode
        else:
            raise RuntimeError('Not Max Heap')
    def addRight(self,rightNode):
        if self.right == None and rightNode.value < self.value:
            self.right = rightNode
        else:
            raise RuntimeError('Not Max Heap')
test = [16,14,10,8,7,9,3,2,4,1]
def addIntoheap(nums,root):
    rootNode = Node(nums[root-1])
    if root*2<=len(nums):
        leftheap = addIntoheap(nums,root*2)
        rootNode.addLeft(leftheap)
    if root*2+1<=len(nums):
        rightHeap = addIntoheap(nums,root*2+1)
        rootNode.addRight(rightHeap)
    return rootNode
try:
    root = addIntoheap(test,1)
except RuntimeError:
    print('not max heap')
    exit(1)
def Fshow(root):
    print(root.value)
    if root.left!=None:
        Fshow(root.left)
    if root.right!=None:
        Fshow(root.right)
def Mshow(root):
    if root.left!=None:
        Mshow(root.left)
    print(root.value)
    if root.right!=None:
        Mshow(root.right)

def Rshow(root):
    if root.left!=None:
        Rshow(root.left)
    if root.right!=None:
        Rshow(root.right)
    print(root.value)


#print(root.left.value)
#print(root.right.value)
Fshow(root)
print('*'*20)
Mshow(root)
print('*'*20)
Rshow(root)
