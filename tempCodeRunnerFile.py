
H, W, N = map(int, input().split())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)
print(R)
print(C)

Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
Cs = sorted(set(C))


print(Rs)
print(Cs)

# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
Rd = {x: i for i, x in enumerate(Rs, 1)}
print(Rd)
Cd = {x: i for i, x in enumerate(Cs, 1)}
print(Cd)
for r, c in zip(R, C):
    print(Rd[r], Cd[c])