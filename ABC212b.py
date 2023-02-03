
di = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 0}
s = input()
x1, x2, x3, x4 = int(s[0]), int(s[1]), int(s[2]), int(s[3])

if x1 == x2 == x3 == x4:
    print("Weak")
elif di[x1] == x2 and di[x2] == x3 and di[x3] == x4:
    print("Weak")
else:
    print("Strong")
