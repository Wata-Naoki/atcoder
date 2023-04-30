x, y, z = map(int, input().split())

origin = 0

if 0 < y < x < z or 0 < y < z < x or x < z < y < 0 or z < x < y < 0:
    print(-1)
elif x < y < 0 < z or z < 0 < y < x:
    print(2 * abs(z) + abs(x))
else:
    print(abs(x))
