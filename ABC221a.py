a, b = map(int, input().split())

if a == b:
    print(1)
else:
    ans = 32**(a-b)
    print(ans)
