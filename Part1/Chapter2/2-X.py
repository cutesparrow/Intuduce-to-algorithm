#2-1
#a. sort a sublist which is k length need k^2 using insertion sort. and there is n/k sublists, so it need nk.
#b. merge n/k sublists need lg(n/k) and make them sorted need n.
#c. if nk+nlg(n/k) == nlg(n): nk+nlgn -nlgk == nlgn ---> nk-nlgk should bigger than 0
#d. Choose 
#k
#k be the largest length of sublist on which insertion sort is faster than merge sort.
#2-4
#reversed sorted list
#d

#divide and conquer
count = 0
def mergeSort(nums):
    global count
    sub1 = nums[:int(len(nums)/2)]
    sub2 = nums[int(len(nums)/2):]
    if len(sub1)>1:
        mergeSort(sub1)
    if len(sub2)>1:
        mergeSort(sub2)
    i=j=k = 0
    while i<len(sub1) and j<len(sub2):
        if sub1[i] <= sub2[j]:
            nums[k] = sub1[i]
            i+=1
            k+=1
        else:
            nums[k] = sub2[j]
            count+=len(sub1) - i
            print(k,i,j,count,sub1[i],sub2[j])
            k+=1
            j+=1
    for m in range(i,len(sub1)):
        nums[k] = sub1[m]
        k+=1
    for n in range(j,len(sub2)):
        nums[k] = sub2[n]
        k+=1
b = [2,3,8,6,1]
b = [1,222,213,12,32,32,3,2,32,4,325,43,5,34,654,67,5,76,57,3434,2,1,2,5,3,2,54,22]
mergeSort(b)
print(count)
print(b)
