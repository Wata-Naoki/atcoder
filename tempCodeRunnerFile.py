s=input()
a, b=map(int, input().split())
tmp_b=s[a]
s[a]=s[tmp_b]
s[b]=s[a]
print(s)