
n = int(input())
n_list = [int(v) for v in input().split()]
ans=0
for val in n_list:
    if val >10:
        ans +=val-10
print(ans)
    
        