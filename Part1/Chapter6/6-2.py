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

root = addIntoheap(test,1)
from queue import Queue
def showHeapWidthFirst(rootNode):
    queue = Queue()
    queue.put([rootNode])
    def BFS():
        nonlocal queue
        readyToShow = queue.get()
        nextLine = []
        for i in readyToShow:
            print(i.value,end=' ')
            if i.left:
                nextLine.append(i.left)
            if i.right:
                nextLine.append(i.right)
        print('\n',end='')
        queue.put(nextLine)
        if len(nextLine) == 0 :
            return
        BFS()
    BFS()
showHeapWidthFirst(root)
def maxHeapify(nums,i):
    l = i*2+1
    r = i*2+2
    if l<=len(nums) and nums[l]>nums[i]:
        largest = l
    else:
        largest = i
    if r<=len(nums) and nums[r]>nums[largest]:
        largest = r
    if largest != i:
        nums[i],nums[largest] = nums[largest],nums[i]
        maxHeapify(nums,largest)

a = [16,4,10,14,7,9,3,2,8,1]
maxHeapify(a,1)
print(a)
def minHeapify(nums,i):
    l = i*2+1
    r = i*2+2
    if l<=len(nums) and nums[l]<nums[i]:
        smallest = l
    else:
        smallest = i
    if r<=len(nums) and nums[r]<nums[smallest]:
        smallest = r
    if smallest != i:
        nums[i],nums[smallest] = nums[smallest],nums[i]
        minHeapify(nums,smallest)
a = [1,10,3,4,5,6,7,8,9,11]
minHeapify(a,1)
print(a)


