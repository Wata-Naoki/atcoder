x, y, n = map(int, input().split())
a = x * n
b = (n // 3) * y + (n % 3) * x
print(min(a, b))
