n = int(input())
p = 0
flag = True
for i in range(1, n + 1):
    if n % i == 0:
        p += 1
    if 2 < p:
        flag = False
        break
print("素数" if flag else "素数じゃない")
