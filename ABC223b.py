
s = input()

s_list = []

for i in range(len(s)):
    s = s[1:]+s[0]
    s_list.append(s)

s_list.sort()
print(s_list[0])
print(s_list[-1])
