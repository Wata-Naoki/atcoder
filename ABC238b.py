n=int(input())
nl=[int(n) for n in input().split()]
b=[0, 360]

cur_angle=0
for val in nl:
    cur_angle+=val
    cur_angle%=360
    b.append(cur_angle)
b.sort()
c=[b[i+1] - b[i] for i in range(len(b)-1)]
print(max(c))