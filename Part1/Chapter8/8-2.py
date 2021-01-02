#count sort
def countingSort(nums,k):
    countList = [0 for i in range(k+1)]
    for i in nums:
        countList[i] += 1
#    for i in range(1,k):
#        countList[i] += countList[i-1]
    result = []
    for i in range(k):
        for j in range(countList[i]):
            result.append(i)
    return result
a = [2,5,3,0,2,3,0,3]
print(countingSort(a,6))
