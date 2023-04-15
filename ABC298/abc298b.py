n = int(input())
a = []
for i in range(n):
    a.append([x for x in input().split()])
b = []
for i in range(n):
    b.append([x for x in input().split()])
tmp_b = b
print(a)
print(b)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] == "1" and b[k][i] == "1":
                b[k][i] = True

for k in range(n):
    for h in range(n):
        for t in range(n):
            a[h][t] = a[t][h]
    for z in range(n):
        for g in range(n):
            for d in range(n):
                if a[g][d] == "1" and b[z][g] == "1":
                    b[z][g] = True


print(a)
print(b)

count = 0
sub_count = 0
for i in range(n):
    for j in range(n):
        if tmp_b[i][j] == "1":
            sub_count += 1
        if tmp_b[i][j] == "1" and b[i][j] == True:
            count += 1
if count == sub_count:
    print("Yes")
else:
    print("No")