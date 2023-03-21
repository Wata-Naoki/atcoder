s=input()
# 大文字が何番目にあるかを調べる
ans=0
for i, v in enumerate(s):
    if v.isupper():
        ans+=i+1
        break
print(ans)