a, b, c, d = map(int, input().split())


l_max = max(a, c)
r_min = min(b, d)

if r_min - l_max > 0:
    print(r_min-l_max)
else:
    print(0)
