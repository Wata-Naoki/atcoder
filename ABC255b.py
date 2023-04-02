n, k = map(int, input().split())
a = [int(num) for num in input().split()]

p = [[0, 0]]

for i in range(n):
    x, y = map(int, input().split())
    p.append([x, y])

dist = [[0] * (n + 1) for i in range(k)]

from math import sqrt


def CalcDist(a, b):
    return sqrt((p[a][0] - p[b][0]) ** 2 + (p[a][1] - p[b][1]) ** 2)


for Gyou in range(k):
    for Retu in range(1, n + 1):
        dist[Gyou][Retu] = CalcDist(a[Gyou], Retu)

RetuMin = [0] * (n + 1)


for Retu in range(1, n + 1):
    d = 10**10
    for Gyou in range(k):
        d = min(d, dist[Gyou][Retu])

    RetuMin[Retu] = d
print(max(RetuMin))
