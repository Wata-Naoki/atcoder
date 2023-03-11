
# 回文の問題

x=int(input().split())

x=str(x)
flag=False
# xが回文かどうかを判定する
for i in range(len(x)//2):
    if x[i]!=x[-i-1]:
        flag=True
        break
print('Yes' if flag else 'No')

# 回文判定の別解
