#divide and conquer
def mergeSort(nums):
    sub1 = nums[:int(len(nums)/2)]
    sub2 = nums[int(len(nums)/2):]
    if len(sub1)>1:
        mergeSort(sub1)
    if len(sub2)>1:
        mergeSort(sub2)
    i=j=k = 0
    while i<len(sub1) and j<len(sub2):
        if sub1[i] < sub2[j]:
            nums[k] = sub1[i]
            i+=1
            k+=1
        else:
            nums[k] = sub2[j]
            j+=1
            k+=1
    for m in range(i,len(sub1)):
        nums[k] = sub1[m]
        k+=1
    for n in range(j,len(sub2)):
        nums[k] = sub2[n]
        k+=1

a = [1,222,213,12,32,32,3,2,32,4,325,43,5,34,654,67,5,76,57,3434,2,1,2,5,3,2,54,22]
mergeSort(a)
print(a)
#binarysearch
def binarySearch(nums,value):
    if len(nums) == 1 and nums[0] != value:
        raise RuntimeError('not found')
    if value < nums[int(len(nums)/2)]:
        return binarySearch(nums[:int(len(nums)/2)],value)
    elif value > nums[int(len(nums)/2)]:
        return int(len(nums)/2)+binarySearch(nums[int(len(nums)/2):],value)
    
    elif value == nums[int(len(nums)/2)]:
        return int(len(nums)/2)

a = [1,2,3,4,5,6,7,8,9,10]
value = 10 
try:
    result = binarySearch(a,value)
except RuntimeError:
    result = None
print(result)
