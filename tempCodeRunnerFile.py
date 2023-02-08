s, t = map(str, input().split())
flag = True
for i in range(len(s)-1):
    tmp = [s[i], t[i]]
    # アルファベットの順番を入れ替える
    tmp.sort()
    print(tmp)
    if tmp[0] != s[i]:
        flag = False
        break
print("Yes" if flag else "No")
