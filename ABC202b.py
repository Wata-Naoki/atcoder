

dict_rev = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
a = input()
a = a[::-1]
ans_val = ''
for v in a:
    ans_val += dict_rev[v]
print(ans_val)


# dict_revのkeyをforで回す
