# quick sort
def quickSort(nums,p,r):
    if p<r:
        q = partition(nums,p,r)
        quickSort(nums,p,q-1)
        quickSort(nums,q+1,r)

def partition(nums,p,r):
    x = nums[r]
    i = p - 1
    for j in range(p,r):
        if nums[j] < x:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[r] = nums[r],nums[i+1]
    return i+1
a = [2,8,7,1,3,5,6,4]
partition(a,0,len(a)-1)
print(a)
quickSort(a,0,len(a)-1)
print(a)
#random choose a num and exchange with the nums[r] which could make this algorithm became kind of a random algorithm.
#只要划分是常数比例的，那么快速排序的时间复杂度就一直是nlgn
