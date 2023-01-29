a, b, c, d = map(int, input().split())

count = -1
for i in range(10**6):
    if a + (i*b) <= (i*c) * d:
        count = i
        break

print(count)
