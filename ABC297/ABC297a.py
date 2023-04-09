n, d = map(int, input().split())
t = [int(x) for x in input().split()]

ans=0
for i in range(n):
    if i >0:
        print(t[i]-t[i-1])
        if t[i] - t[i-1]<=d:

            print(t[i])
            exit()

print(-1)

    