N,Q=[int(nq) for nq in input().split()]
# 二次元リスト Aで N個の数列を管理
A=[]
for _ in range(N):
    l,*a = [int(la) for la in input().split()]
    A.append(a)

for _ in range(Q):
    s,t=[int(st) for st in input().split()]
    print(A[s-1][t-1])