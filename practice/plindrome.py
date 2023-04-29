def judge_palindrome(n):
    flag = False
    # if n == n[::-1]:
    #     flag = True
    if n == "".join(reversed(n)):
        flag = True
    return flag


n = input()
result = judge_palindrome(n)
print("回文" if result else "回文じゃない")
