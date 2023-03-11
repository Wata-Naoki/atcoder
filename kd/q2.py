

# フィボナッチ数列の問題。段数が入力されるので、その段数のフィボナッチ数を出力する。
# 例えば、入力が 5 なら、5 段目のフィボナッチ数を出力する。
# 4の場合は、3+2=5
# 5の場合は、5+3=8


n=int(input())

if n <= 1:
    print(n)
num1, num2=0, 1
for i in range(n):
    num1, num2=num2, num1+num2

print(num2)
n=[]






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
    if flag == False:
        break
print(n)


