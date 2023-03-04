s=input()
a, b=map(int, input().split())
tmp_b=s[a]
s[a]=s[b]
s[b]=tmp_b
print(s)