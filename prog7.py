myString = input()
tempString = myString[0]

for i in myString:
    if i == myString[0]:
        newString = myString.replace(i,"$")
newList = list(newString)
newList[0] = tempString
for x in newList:
    print(x, end="")