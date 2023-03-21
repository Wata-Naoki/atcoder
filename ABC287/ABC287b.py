
n, m = map(int, input().split())
s = []
for _ in range(n):
    s.append(input())

t = []
for _ in range(m):
    t.append(input())

count = 0
for i in range(n):
    for j in range(m):
        if t[j] in s[i][-3:]:
            count += 1
            break

print(count)
