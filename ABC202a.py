dice_rev = {'1': 6, '2': 5, '3': 4, '4': 3, '5': 2, '6': 1}
n_list = [v for v in input().split()]
ans = 0
for v in n_list:
    ans += dice_rev[v]
print(ans)
