n, a, b = map(int, input().split())
c = [int(n) for n in input().split()]

for ind, val in enumerate(c):
    if val == a + b:
        print(ind + 1)
