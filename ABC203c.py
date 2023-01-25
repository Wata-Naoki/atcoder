n, k = map(int, input().split())

mat = []

for _ in range(n):
    a, b = map(int, input().split())
    mat.append((a, b))
mat.sort()
now = k

for i in range(n):
    a, b = mat[i]
    if now >= a:
        now += b
        print(now)
    else:
        break
print(now)
