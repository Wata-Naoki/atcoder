
rec_x=[]
rec_y=[]
for i in range(3):
    x, y=map(int, input().split())
    rec_x.append(x)
    rec_y.append(y)

ans=[0, 0]

for x, y in zip(rec_x, rec_y):
    if rec_x.count(x)==1:
        ans[0]=str(x)
    if rec_y.count(y)==1:
        ans[1]=str(y)
print(' '.join(ans))

