#最大子数组
#divide and conquer
def findCrossMax(nums,low,mid,high):
    sums = 0
    maxleft = 0
    for i in range(mid,low-1,-1):
        sums += nums[i]
        if sums>maxleft:
            maxleft = sums
    maxright = 0
    sums = 0
    for i in range(mid+1,high+1):
        sums += nums[i]
        if sums > maxright:
            maxright= sums
    return maxleft+maxright
def findMaxSub(nums,low,high):
    if low == high:
        return nums[low]
    mid = int((low+high)/2)
    leftMax = findMaxSub(nums,low,mid)
    rightMax = findMaxSub(nums,mid+1,high)
    midMax = findCrossMax(nums,low,mid,high)
    return max(leftMax,rightMax,midMax)
a = [13,-3,-25,20,-3,-16,-23, 18,20,-7,12 ,-5,-22,15,-4,7]
print(findMaxSub(a,0,len(a)-1))
#dp
def findMax(nums):
    max_ = 0
    sum_ = 0
    left = 0
    right = 0
    for i in range(len(nums)):
        sum_ += nums[i]
        if sum_ < 0:
            sum_ = 0
            left = i+1
        if max_<sum_:
            max_ = sum_
            right = i
    return (max_,left,right)
print(findMax(a))
