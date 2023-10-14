def candies(days,a,b):
    for i in range(days):
        t1 = (2*a) + b + 1
        t2 = (3*b) + a + 1
        a= t1
        b = t2
    return [a,b]
n = int(input())
ca = input()
a = ca.split()
res = candies(n,int(a[0]),int(a[1]))
mod = 10**9 + 7
print(res[0]%mod)
print(res[1]%mod)