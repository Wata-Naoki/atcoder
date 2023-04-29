def judge(n):
    flag = True
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if 2 < count:
            flag = False
            break
    ans = "素数" if flag else "素数じゃない"
    return ans


n = int(input())
print(judge(n))
