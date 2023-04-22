n = input()
s = input()
s_list = list(s)
ans = []
for ind, val in enumerate(s_list):
    if val == "|":
        ans.append(ind)

if "*" in s[ans[0] : ans[1]]:
    print("in")
else:
    print("out")
