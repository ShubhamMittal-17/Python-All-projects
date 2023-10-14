mylist=["a","x","y","z","a","y","2","x","5"]
for o in mylist:
    i=mylist.count(o)
    if i>1:
        mylist.remove(o)
print(mylist)


