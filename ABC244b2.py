n=int(input())
s=input()

d=0
t=[(1, 0), (0, -1), (-1, 0), (0, 1)]
x, y=0, 0
for c in s:
    if c == 'S':
        dx, dy=t[d]
        x+=dx
        y+=dy
    elif c == 'R':
        d += 1
        d %= 4
print(x, y)