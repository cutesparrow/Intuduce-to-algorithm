# insertion sort
def insertionSort(nums):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                nums.insert(j, nums[i])
                del nums[i + 1]


a = [2, 1, 3, 4, 2, 4, 6, 4, 2]
insertionSort(a)
print(a)
# 循环不变式1. 开始正确，2.如果循环之前正确，循环之后也正确，3.结束时正确
b = [31, 41, 59, 26, 41, 58]
insertionSort(b)
print(b)


# 2.1-2
def insertionSortReversed(nums):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                nums.insert(j, nums[i])
                del nums[i + 1]


insertionSortReversed(b)
print(b)


# 2.1-3
def findValue(nums, value):
    for j in range(len(nums)):
        if nums[j] == value:
            return j
    return None


print(findValue(a, 6))


# 2.1-4
def addTwoBinary(nums1, nums2):
    extra = 0
    sum = []
    for i in range(len(nums1) - 1, -1, -1):
        result = nums1[i] + nums2[i] + extra
        if result == 0:
            sum.insert(0, result)
            extra = 0
        elif result == 1:
            sum.insert(0, result)
            extra = 0
        elif result == 2:
            sum.insert(0, 0)
            extra = 1
        elif result == 3:
            sum.insert(0, 1)
            extra = 1
    if extra == 1:
        sum.insert(0, 1)
    return sum


print(1, 2, 3, 4)
nums1 = [1, 0, 1, 0, 1, 0]
nums2 = [1, 1, 1, 0, 0, 1]
print(addTwoBinary(nums1, nums2))
