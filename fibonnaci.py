i1=0
i2=1
lim=int(input("Enter a value:"))
print(i1,i2,end=" ")
for i in range(lim):
    i3=i1+i2
    print(i3, end = " ")
    i1=i2
    i2=i3

