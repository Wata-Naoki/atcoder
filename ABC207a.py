
import itertools
a, b, c = map(int, input().split())
ans = []
all = itertools.permutations((a, b, c), 2)
for x in all:
    ans.append(sum(list(x)))

print(max(ans))
