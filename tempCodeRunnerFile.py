s = list(input())
print(s)
count = 1
ans = ""
while True:
    for val in s:
        ans += val
        if len(ans) == 6:
            print(ans)
            break
