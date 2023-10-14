a=list(input())
b=list() 
for i in range(1,len(a)+1):
    b.append(a[-i])
for i in b:
    print(i,end="")