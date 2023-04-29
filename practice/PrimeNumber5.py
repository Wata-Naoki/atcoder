n = int(input())
count = 0
trigger = 2
flag = True
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
    if trigger < count:
        flag = False
        break

print("素数" if flag else "素数じゃない")
