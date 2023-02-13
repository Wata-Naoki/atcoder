n = input()
if len(n) == 4:
    print(n)
else:
    while len(n) != 4:
        n = '0' + n
    print(n)
