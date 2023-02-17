N = int(input())
S = set()

for _ in range(N):
    l, *A = map(int, input().split())  
    print(A, 'brfor')
    A = tuple(A)  
    print(A, '111')
    S.add(A)

print(len(S))