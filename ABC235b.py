n=int(input())
n_list=[int(v) for v in input().split()]
# print(n_list)
ans=0
for val in n_list:
    if ans < val:
        ans=val
    else:
        break
print(ans)
