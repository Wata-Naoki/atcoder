n = int(input())

for i in range(1, n + 1):
    if i % 5 == 0 and i % 3 == 0:
        print("{}:FizzBuzz".format(i))
    elif i % 5 == 0:
        print("{}:Buzz".format(i))
    elif i % 3 == 0:
        print("{}:Fizz".format(i))
    else:
        print(i)
