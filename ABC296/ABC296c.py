n, x = map(int, input().split())
a = set([int(n) for n in input().split()])
print(a)
flag = False
for i in a:
    if i + x in a:
        flag = True
        break

print("Yes" if flag else "No")
# TLEになってしまた
# set型にして、重複した数字は計算しないようにする
# v1 - v2 = x があるかなので、式変形して、v1=x+v2がaのリストにあればおけなんよね
