while True:
    x=int(input("How many times do you want to pat the cat's head? "))
    if x>0:
        break
print("*pats*, cat: meow!\n"*x, end="")
