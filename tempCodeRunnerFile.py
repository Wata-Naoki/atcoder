import math
x=int(input())
print(x)
if x <0:
    tmp=math.ceil(abs(x/10))
    x=-tmp
else:
    x=x//10
    print(x)



print(x)