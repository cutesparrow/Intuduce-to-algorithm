#heap sorted

def maxHeapify(nums,i):
    l = i*2+1
    r = i*2+2
    print(l,r)
    if l<len(nums) and nums[l]>nums[i]:
        largest = l
    else:
        largest = i
    if r<len(nums) and nums[r]>nums[largest]:
        largest = r
    if largest != i:
        nums[i],nums[largest] = nums[largest],nums[i]
        maxHeapify(nums,largest)
a = [12,1,2,3,2123,21,31,23,12,3214,32,4,3]
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
print(heapSort(a))

