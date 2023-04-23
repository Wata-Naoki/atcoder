dic = {}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
ls_length = len(days)
for ind, val in enumerate(days):
    dic[val] = ls_length - ind
s = input()
print(dic[s])
