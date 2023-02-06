
n=int(input())

for i in range(n):
    if n<=1:
        print(0)
        break
    if 2**i>n:
        print(i-1)
        break