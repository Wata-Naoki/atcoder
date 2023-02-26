n=int(input())
x=[int(i) for i in input().split()]
x.sort()
# print(x)
for i in range(n):
    x.pop(0)
    x.pop(-1)
# 小数点も出力
print(sum(x)/len(x))