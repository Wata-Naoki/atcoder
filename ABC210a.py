
n, a, x, y = map(int, input().split())

ans = (a*x)+((n-a)*y) if n > a else n*x
print(ans)
