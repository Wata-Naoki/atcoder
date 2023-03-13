n=int(input())
s=input()
x, y=0
num=1
for val in s:
    if val=='R':
        if num==4:
            num=1
        else:
            num+=1
    elif num==1:
        x+=1
    elif num==2:
        y-=1
    elif num==3:
        x-=1
    else:
        y+=1
print(x, y)