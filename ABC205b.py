
n = int(input())
n_list = [int(num) for num in input().split()]
comp_list = [int(num) for num in range(1, n+1)]
flag = True
for val in comp_list:
    if val not in n_list:
        flag = False
        break
print('Yes' if flag else 'No')
