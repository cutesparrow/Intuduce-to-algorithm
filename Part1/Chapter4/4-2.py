#strassen
import numpy

a =     [[1,2,3],
        [2,3,4],
        [3,4,5]]

b = [
    [1,2,3],
    [4,2,1],
    [4,2,9]
    ]
def muti(a,b):
    result = numpy.zeros((3,3),int)
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(a)):
                result[i][j] += a[i][k]*b[k][j]
                print(result)
    return result

print(muti(a,b))
