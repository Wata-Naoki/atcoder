
a, b, c = map(int, input().split())
i = 1
ans = 0
while ans < b:
    if a <= i * c <= b:
        ans = i*c
        break
    i += 1
print(ans)
