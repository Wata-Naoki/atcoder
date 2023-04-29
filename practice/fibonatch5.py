# def cal(n):
#     if n <= 1:
#         return n
#     num1, num2 = 0, 1
#     for i in range(n):
#         num1, num2 = num2, num1 + num2
#     return num2


# n = int(input())
# result = cal(n)
# print(result)


# def solution(n):
#     flag = False
#     if n == "".join(reversed(n)):
#         flag = True
#     return flag


# n = input()
# print(solution(n))

n = [2, 5, 3, 8]
n.sort()
print(n)
