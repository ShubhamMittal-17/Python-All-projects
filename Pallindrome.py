a=input(str())
a=list(a)
b=list()
for i in range(1,len(a)+1):
    b.append(a[-i])
if a==b:
    print("It is a pallindrome.")
else:
    print("Not a pallindrome.")