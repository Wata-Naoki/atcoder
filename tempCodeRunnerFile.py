s=input()
a, b=map(int, input().split())
s_list=list(s)
tmp_a=s[a-1]
tmp_b=s[b-1]
# s[a]=tmp_b
s_list[a-1]=tmp_b
s_list[b-1]=tmp_a
ans="".join(s_list)
print(ans)