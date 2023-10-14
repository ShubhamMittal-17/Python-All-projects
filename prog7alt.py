newstring=input()
firstchar=newstring[0]
modstr= firstchar+ newstring[1:].replace(firstchar,"$")
print(modstr)
