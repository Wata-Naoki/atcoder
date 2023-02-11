
a, b, c = map(int, input().split())
i = 1
ans = 0
flag = False
while ans < b:
    ans = i*c
    if a <= i * c <= b:
        flag = True
        break
    i += 1

print(ans if flag else -1)
