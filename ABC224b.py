h, w = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(h)]

for r2 in range(h):
    for r1 in range(r2):
        for c2 in range(w):
            for c1 in range(c2):
                if a[r1][c1] + a[r2][c2] > a[r1][c2] + a[r2][c1]:

                    print('No')
                    exit()

print('Yes')
