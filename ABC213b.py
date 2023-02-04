n = int(input())

a_list = [int(n) for n in input().split()]
tmp_list = a_list.copy()
# ソートしたいので、a_listをソートする
a_list.sort()
# print(a_list)
# print(tmp_list)
print(tmp_list.index(a_list[-2])+1)
