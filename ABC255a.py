r, c = map(int, input().split())
a_list = []
for i in range(2):
    a_list.append([int(num) for num in input().split()])

print(a_list[r - 1][c - 1])
