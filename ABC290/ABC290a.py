a, b=map(int, input().split())
a_list=[int(x) for x in input().split()]
b_List=[int(x) for x in input().split()]

ans=0
for i in b_List:
    ans+=a_list[i-1]
print(ans)




