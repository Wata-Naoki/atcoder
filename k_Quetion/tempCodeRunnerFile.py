
n=input()
# 隣接した文字列を削除する
# 隣接した文字列がなくなるまで繰り返す
while True:
    flag=False
    for i in range(len(n)-1):
        if n[i]==n[i+1]:
            n=n[:i]+n[i+2:]
            flag=True
            break
    if not flag:
        break
print(n)
