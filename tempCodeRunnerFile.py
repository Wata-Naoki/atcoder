s = list(input())
s_int_list = [int(x) for x in s]
s_int_list.sort()
print(s_int_list)
ans = 0
for i in range(len(s)):
    if i not in s_int_list:
        ans = i
        break
print(ans)
