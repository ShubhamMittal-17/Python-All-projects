def main():
    x=int(input("Input height: "))
    y=int(input("Input width: "))
    print_square(x,y)

def print_square(n,m):
     for _ in range(n):
          print("[#]"*m)

main()  