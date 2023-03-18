a=[int(v) for v in input().split()]

ans=a[0]
for i in range(2):
    ans=a[ans]

print(ans)