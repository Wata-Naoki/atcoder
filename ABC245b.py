
n=int(input())
a_list=[int(n) for n in input().split()]
ans=0

for i in range(n+1):
    if i not in a_list:
        ans=i
        break
print(ans)
