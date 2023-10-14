i=int(input("Enter the length of 1st array:"))
a=1
array1=[]
while a<=i:
    item=input("Enter item: "+str(a)+" ",)
    array1.append(item)
    a+=1
array1.sort()
print(array1)
q=int(input("Enter the length of 2nd array:"))
b=1
array2=[]
while b<=q:
    item=input("Enter item: "+str(b)+" ",)
    array2.append(item)
    b+=1
array2.sort()
print(array2)

array1.extend(array2)
array1.sort()
print(array1)