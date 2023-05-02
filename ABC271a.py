n = int(input())
n = hex(n)
n = n[2:]
n = n.upper()
if len(n) == 1:
    print("0" + n)
else:
    print(n)
