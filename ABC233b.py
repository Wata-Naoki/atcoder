l,r=map(int, input().split())
s=input()
new_s=s[l-1:r]
ans=s[:l-1]+new_s[::-1]+s[r:]
print(ans)