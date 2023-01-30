
import math

p = int(input())

ans = 0

for i in range(10, 0, -1):
    coin = math.factorial(i)

    while coin <= p:
        print(coin)

        ans += 1
        p -= coin

print(ans)
