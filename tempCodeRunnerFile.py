

n, m = map(int, input().split())
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]


diff = []

for i in range(n):
    for j in range(m):
        diff.append(abs(a[i]-b[j]))

# print(diff)
print(min(diff))
