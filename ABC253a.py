a, b, c = map(int, input().split())
sort_list = [a, b, c]
sort_list.sort()
# print(sort_list)
flag = False
if sort_list[1] == b:
    flag = True
print("Yes" if flag else "No")
