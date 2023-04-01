n = int(input())
s = input()
flag = True
if "MM" in s or "FF" in s:
    flag = False
print('Yes' if flag else 'No')