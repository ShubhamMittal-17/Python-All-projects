N = int(input())
l1=[]
for i in range(N):
    x=input()
    x=x.split()
    if "append" in x:
        l1.append(x[1])
    if "insert" in x:
        l1.insert(int(x[1]), int(x[2]))
    if "print" in x:
        print(l1)
    if "remove" in x:
        l1.remove(int(x[1]))   
    if "sort" in x:
        l1.sort()
    if "pop" in x:
        l1.pop()
    if "reverse" in x:
        l1.sort(reverse=True)     
print(l1)   