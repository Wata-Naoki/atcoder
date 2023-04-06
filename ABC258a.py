k = int(input())
hour = 21
minutes = 0
ans_hour = hour + k // 60
ans_minutes = minutes + k % 60
if ans_minutes < 10:
    print("{}:0{}".format(ans_hour, ans_minutes))
else:
    print("{}:{}".format(ans_hour, ans_minutes))
