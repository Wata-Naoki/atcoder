
n = int(input())

ans = []

for _ in range(n):
    ans.append(input())

if len(ans) == 1 and ans.count('For') == 1:
    print('Yes')
elif ans.count('For') > n//2:
    print('Yes')
else:
    print('No')

    



        