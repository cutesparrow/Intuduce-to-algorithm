#什么时候适合使用动态规划呢：
#1. 求解最优问题
#2. 有需要重复计算的子问题
def cut(p,n):
    if n == 0:
        return 0
    q = -2e10
    for i in range(1,n+1):
        q = max(q,p[i-1]+cut(p,n-i))
    return q

p_nums = [1,5,8,9,10,17,17,20,24,30]
print(cut(p_nums,7))


def memoized_cut(p,n):
    memoized_list = [-2e10 for i in range(n+1)]
    return memoized_main(p,n,memoized_list) 

def memoized_main(p,n,r):
    if r[n] > -2e10:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -2e10
        for i in range(1,n+1):
            q = max(q,p[i-1]+memoized_main(p,n-i,r))
    r[n] = q
    return q
print(memoized_cut(p_nums,7))

def eaiset_cut(p,n):
    r = [None for i in range(n+1)]
    r[0] = 0
    for i in range(1,n+1):
        q = -2e10
        for j in range(1,i+1):
            q = max(q,p[i-1]+r[i-j])
        r[i] = q
    return r[n]
