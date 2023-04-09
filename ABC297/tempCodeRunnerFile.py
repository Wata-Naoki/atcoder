s = input()
s_list = list(s)
b_list = []
r_list = []
k = []

for ind, val in enumerate(s_list):
    if val == "B":
        b_list.append([val, ind + 1])
    if val == "R":
        r_list.append(ind + 1)
    if val == "K":
        k.append(ind + 1)

if (
    b_list[0][1] % 2 == 0
    and b_list[1][1] % 2 == 1
    or b_list[1][1] % 2 == 0
    and b_list[0][1] % 2 == 1
):
    pass
else:
    print("No")
    exit()
# print(r_list, k)
if r_list[0] < k[0] < r_list[1]:
    print("Yes")
else:
    print("No")
