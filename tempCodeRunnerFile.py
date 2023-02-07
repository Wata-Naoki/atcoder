
n = int(input())
n_list = []

for i in range(n):
    s, t = input().split()
    n_list.append(s+t)

if len(n_list) == len(set(n_list)):
    print('No')
else:
    print('Yes')
    
    