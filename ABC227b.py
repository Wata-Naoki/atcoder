
def cal(a, b):
    return 4*a*b+3*a+3*b


n=int(input())
s_list=[int(x) for x in input().split()]
t=set()


for a in range(1, 1001):
    for b in range(1, 1001):
        t.add(cal(a, b))

ans =0

for v in s_list:
    if v not in t:
        ans+=1
print(ans)
