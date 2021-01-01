
#heap sorted

def maxHeapify(nums,i):
    l = i*2+1
    r = i*2+2
    if l<len(nums) and nums[l]>nums[i]:
        largest = l
    else:
        largest = i
    if r<len(nums) and nums[r]>nums[largest]:
        largest = r
    if largest != i:
        nums[i],nums[largest] = nums[largest],nums[i]
        maxHeapify(nums,largest)
a = [16,14,10,8,7,9,3,2,4,1] 
def makeHeap(nums):
    size = len(nums)
    for i in range(int((size-1)/2),-1,-1):
        maxHeapify(nums,i)
makeHeap(a)
def heapSort(nums):
    makeHeap(nums)
    result = []
    for i in range(len(nums)-1,-1,-1):
        nums[0],nums[-1] = nums[-1],nums[0]
        result.append(nums[-1])
        del nums[-1]
        maxHeapify(nums,0)
    return result
def heapMaximum(nums):
    return nums[0]
def heapExtractMax(nums):
    if len(nums) == 0:
        raise RuntimeError('heap underflow')
    max = nums[0]
    nums[0] = nums[-1]
    del nums[-1]
    maxHeapify(nums,0)
    return max
def heapIncreaseKey(nums,i,key):
    if key<nums[i]:
        raise RuntimeError('new key shoule be bigger than current one')
    nums[i] = key
    while i > 0 and nums[int((i+1)/2)-1] < nums[i]:
        nums[int((i+1)/2)-1],nums[i] = nums[i],nums[int((i+1)/2)-1] 
        i = int((i+1)/2-1)

heapIncreaseKey(a,8,15)
print(a)
def maxHeapInsert(nums,key):
    nums.append(key)
    heapIncreaseKey(nums,len(nums)-1,key)
maxHeapInsert(a,18)
print(a)
