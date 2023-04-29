n = int(input())

if n <= 1:
    print(n)
else:
    num1, num2 = 0, 1
    for i in range(n):
        num1, num2 = num2, num1 + num2
    print(num2)
