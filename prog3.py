mylist=["abc","xyz","aba","1221"]
for x in mylist:
    if len(x)>=2 and x[0]==x[-1]:
        print(x)
