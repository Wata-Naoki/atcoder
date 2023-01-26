
x, y = map(int, input().split())

if x == y:
    print(x)
else:
    result = [0, 1, 2]
    result.remove(x)
    result.remove(y)
    print(result[0])
