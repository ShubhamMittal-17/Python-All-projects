x= 56

def myfunc():
    global x
    print(100+x)
    x=x+1

myfunc()    
print(x)

print(type(x))
y=7j
print(type(y))

z=range(6)
print(type(z))

a=True
print(type(a))

c=b"hello"
print(type(c))

d=None
print(type(d))

e=bool(5<3)
print(e)