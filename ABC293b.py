
k=int(input())
kl=[int(v) for v in input().split()]
dic={}
for i in range(k):
    dic[i+1]=0

print(dic)
for ind, val in enumerate(kl):
    print(ind, val, dic[val])
    if dic[val]==0:
        dic[val]+=1
    elif dic[val]==1:
        dic[val]-=1 

print(dic)
