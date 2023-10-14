def adjm(n,mar):
    pat = "11"
    res =[]
    for i in range(n):
        if pat in mar[i][1]:
            res.append(False)
        else:
            res.append(True)
    return res
n = int(input())
cases = []
for _ in range(n):
    num = int(input())
    bs = input()
    cases.append([num,bs])
ans = adjm(n,cases)
for i in ans:
    print(i)
        