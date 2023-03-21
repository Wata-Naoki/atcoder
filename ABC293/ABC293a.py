s=input()
l=len(s)
ans=list(s)
for i in range(0, l, 2):
    ans[i], ans[i+1]=s[i+1], s[i]
print(''.join(ans))