import random
print(random.randrange(1,10))

a='''  LLlorem ipsum dolor sit amet
consectetur adipiscing elit,
sed do eiusmod tempor incididunt \n '''
print(a)

print(a[10])  # strings function as an array and we can extract any of its elements

for x in "shubham":
    print(x)

print(len(a))

if "lorm" not in a:
    print("lorm is not present")

print(a.upper(),"\n")
print(a.lower(),"\n")
print(a.strip(),"\n")
print(a.replace("i","k"),"\n")
print(a.split(","),"\n")