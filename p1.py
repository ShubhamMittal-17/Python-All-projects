import math
def dist(inst):
    r = inst.count("R")
    l = inst.count("L")
    e = inst.count("_")
    if l==0 and r ==0 :
        return e
    n1 = abs(r-l)
    return n1+e
s = input()
ans = dist(s)
print(ans)