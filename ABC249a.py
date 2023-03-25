a, b, c, d, e, f, x = map(int, input().split())
res1 = 0
res2 = 0
for t in range(1, x + 1):
    t1 = t % (a + c)
    if 1 <= t1 <= a:
        res1 += b
    t2 = t % (d + f)
    if 1 <= t2 <= d:
        res2 += e

if res1 > res2:
    print("Takahashi")
elif res2 > res1:
    print("Aoki")
else:
    print("Draw")
