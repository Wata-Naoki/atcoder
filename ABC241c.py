n=int(input())

grid=[]
for i in range(n):
    s=input()
    s=list(s)
    grid.append(s)
# print(grid)

def SearchRight(gyou, retu):
    count=0
    for i in range(6):
        if grid[gyou][retu+i]=="#":
            count+=1
    return count 

def SearchDown(gyou, retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu]=="#":
            count+=1
        return count 
def SearchRightDown(gyou, retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu+i]=="#":
            count+=1
    return count

def SearchLeftDown(gyou, retu):
    count=0
    for i in range(6):
        if grid[gyou+i][retu-i]=="#":
            count+=1
    return count

for gyou in range(n):
    for retu in range(n):
        if retu+5 < n:
            if 4 <= SearchRight(gyou, retu):
                print('Yes')
                exit()

        if gyou+5 < n:
            if 4<=SearchDown(gyou, retu ):
                print('Yes')
                exit()
                
        if retu+5 < n and gyou+5<n:
            if 4<=SearchRightDown(gyou, retu):
                print("Yes")
                exit()

        if gyou+5 < n and 0 <= retu -5:
            if 4<=SearchLeftDown(gyou, retu):
                print("Yes")
                exit()

print("No")