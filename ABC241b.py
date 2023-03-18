n, m=map(int, input().split())
a=[x for x in input().split()]
b=[x for x in input().split()]
flag=True
for v in b:
    if v in a:
        a.remove(v)
    else:
        flag=False
print('Yes' if flag else 'No')