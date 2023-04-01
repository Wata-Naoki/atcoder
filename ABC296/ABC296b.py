l = []

for i in range(8):
    n = list(input())
    l.append(n)
# print(l)

alp = []
ind = 9
for j in range(1, 9):
    val = []
    for i in range(97, 106):
        val.append(chr(i) + str(abs(j - ind)))
    alp += [val]

# print(alp)

ans_ind = []
for i in range(8):
    for ind, val in enumerate(l[i]):
        if val == "*":
            ans_ind += [i, ind]
# print(ans_ind)
print(alp[ans_ind[0]][ans_ind[1]])
