s = input()
s_list = list(s)
if s_list[0] == s_list[1] == s_list[2]:
    print(-1)
else:
    for val in s_list:
        if s_list.count(val) == 1:
            print(val)
            break
