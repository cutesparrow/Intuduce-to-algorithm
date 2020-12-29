#2.2-2
#choose sort
def chooseSort(nums):
    for i in range(len(nums)-1):
        for j in range(i,len(nums)):
            if j==i:
                minIndex = j
            else:
                if nums[j]<nums[minIndex]:
                    minIndex = j
        nums[i],nums[minIndex] = nums[minIndex],nums[i]
        print(nums)
a = [2,1,3,4,2,6,23,22,18]
chooseSort(a)
print(a)
#针对特殊情况进行测试，如果符合的话就直接给出预先计算好的答案。
#就是增加常数时间能跑完的代码，用于覆盖一些特例，减少无所谓的循环。
