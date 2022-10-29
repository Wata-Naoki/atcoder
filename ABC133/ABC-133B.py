import math
N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]
count = 0

for i in range(N):
    for j in range(i+1, N):
        ans = 0
        sum = 0
        for k in range(D):
            sum += abs(X[i][k]-X[j][k])**2
        ans = math.sqrt(sum)
        if ans.is_integer():
            count += 1

print(count)
