n = int(input())
p_list = [0] + [0] + list(map(int, input().split()))
i = n

count = 1
while p_list[i] != 1:
    count += 1
    i = p_list[i]
print(count)
