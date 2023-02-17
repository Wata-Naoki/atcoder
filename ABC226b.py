N = int(input())
S = set()

for _ in range(N):
    l, *A = map(int, input().split())  
    # *Aは、リストになっているのでタプルに変換
    A = tuple(A)  
    # print(A, '111')
    S.add(A)

print(len(S))





# n=list(input().split())
# print(n[1:])

