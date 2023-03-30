n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
max_val = max(a)
b.sort()
flag = False
for val in b:
    if max_val == a[val - 1]:
        flag = True

print("Yes" if flag else "No")
