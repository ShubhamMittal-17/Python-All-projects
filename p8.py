def dragon(grid):
    n = len(grid)
    rr = [0]*n
    cc = [0]*n
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                rr[i] = 1
                cc[j] =1
    rc = sum(rr)
    c = sum(cc)
    arrow = min(rc,c)
    return arrow
n = int(input())
grid = []
for i in range(n):
    rr = input().split()
    nn = [int(c) for c in rr]
    grid.append(nn)
res = dragon(grid)
print(res)
    