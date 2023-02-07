n = int(input())

s_set = set()

for _ in range(n):
    s = input()
    s_set.add(s)

print("No" if len(s_set) == n else "Yes")
