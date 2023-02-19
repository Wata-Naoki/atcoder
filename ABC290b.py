

n, k=map(int, input().split())
s=input()

ans=''
count=0
for i, v in enumerate(s):
    if v=='o':
        count+=1
    if count > k:
        ans+='x'
    else:
        ans+=v

print(ans)