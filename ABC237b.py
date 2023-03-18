h, w = map(int, input().split())

tmp=[]
for i in range(h):
    a_tmp=[int(n) for n in input().split()]
    tmp.append(a_tmp)

b=[[0]*h for i in range(w)]

for i in range(w):
    for j in range(h):
        b[i][j]=tmp[j][i]

for i in range(w):
    print(*b[i])