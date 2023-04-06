n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input())))

index = [[i, j] for i in range(n) for j in range(n)]
xy = [[x, y] for x in [0, 1, -1] for y in [0, 1, -1] if not x == y == 0]
l = []
for i in index:
    for x, y in xy:
        x_t, y_t = i[0], i[1]
        r = str(a[x_t][y_t])
        for _ in range(n - 1):
            x_t = (x_t + x) % n
            y_t = (y_t + y) % n
            r += str(a[x_t][y_t])
            l.append(int(r))
print(max(l))
