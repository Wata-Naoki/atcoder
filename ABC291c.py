import collections
n=int(input())
s=input()
x=0
y=0
dic={'R':x+1, 'L':x-1, 'U':y+1, 'D': y-1}

tl=[(0, 0)]
# count=0
for v in s:
    if 'R' == v:
        x=x+1
        tl.append((x, y))
    elif 'L'==v:
        x=x-1
        tl.append((x, y))
    elif 'U' == v:
        y=y+1
        tl.append((x, y))
    elif 'D' ==v:
        y=y-1
        tl.append((x, y))
            
count=collections.Counter(tl)
# print(count.most_common())
# print(count.most_common()[0][1])
freq=count.most_common()[0][1]
print('Yes' if freq>=2 else 'No')
     