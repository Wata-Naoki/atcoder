
def solve():
    n, x=map(int, input().split())
    dp = [[False] * (x +1) for _ in range(n+1)]
   # print(dp)
    dp[0][0] = True

    for i in range(n):
        a, b=map(int, input().split())
        for j in range(x+1):
            if dp[i][j]:
                if j + a <= x:
                    dp[i+1][j+a] = True
                if j + b <= x:
                    dp[i+1][j+b]=True 
    # print('-----------')
   #  print(dp)
    return dp[n][x]

print('Yes' if solve() else 'No')