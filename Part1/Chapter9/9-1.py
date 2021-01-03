# chapter 9
def findMinAndMax(nums):
    if int(len(nums) / 2) * 2 == len(nums):
        minValue = nums[0]
        maxValue = nums[1]
        start = 2
    else:
        minValue, maxValue = nums[0], nums[0]
        start = 1
    print(len(nums))
    for i in range(start, len(nums), 2):
        print(i)
        min, max = (nums[i],
                    nums[i + 1]) if nums[i] < nums[i + 1] else (nums[i + 1],
                                                                nums[i])
        if min < minValue:
            minValue = min
        if max > maxValue:
            maxValue = max
    return minValue, maxValue


def partition(nums, p, r):
    flay = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] < flay:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def select(nums, p, r, i):
    if p == r:
        return nums[p]
    q = partition(nums, p, r)
    k = q - p + 1
    if i == k:
        return nums[q]
    elif i < k:
        return select(nums, p, q - 1, i)
    else:
        return select(nums, q + 1, r, i - k)


a = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 2232, 32, 32, 3, 23, 2, 32, 3, 23, 23, 2, 332
]
print(select(a, 0, len(a) - 1, 12))
