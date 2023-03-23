s = list(input())
s_int_list = [int(x) for x in s]
# print(s_int_list)
ans = 0
for i in range(10):
    if i not in s_int_list:
        ans = i
        break
print(ans)
