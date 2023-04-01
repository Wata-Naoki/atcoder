n, x = map(int, input().split())
a = [int(x) for x in input().split()]

flag = False
for i in range(n):
    for j in range(n):
        if a[i] - a[j] == x:
            flag = True
            break
print("Yes" if flag else "No")
# TLEになってしまた
