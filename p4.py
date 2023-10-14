def calc(mat,q):
    n = len(mat)
    m = len(mat[0])
    pref = [[0]* m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            pref[i][j] = mat[i][j]
            if i > 0:
                pref[i][j]+= pref[i-1][j]
            if j>0:
                pref[i][j] += pref[i][j-1]
            if i>0 and j>0:
                pref[i][j] -= pref[i-1][j-1]
    res = []
    for z in q:
        x1,y1,x2,y2 = z
        sub = pref[x2][y2]
        if x1 > 0:
            sub -= pref[x1-1][y2]
        if y1 >0:
            sub -= pref[x2][y1-1]
        if x1>0 and y1>0:
            sub += pref[x1-1][y1-1]
        res.append(sub)
    return res
nn = input().split()
n = int(nn[0])
q = int(nn[1])
mat = []
que = []
for _ in range(n):
    row = list(map(int,input().split()))
    mat.append(row)
for _ in range(q):
    x1,y1,x2,y2 = map(int,input().split())
    que.append([x1,y1,x2,y2])
ans = calc(mat,que)
for i in ans:
    print(i)