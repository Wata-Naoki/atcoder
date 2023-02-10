sd = {}

for i in range(1, 4):
    sd[i] = input()

t = input()
ans = ''
for val in t:
    ans += sd[int(val)]
print(ans)
