n = int(input())

ans = ''

while n > 0:
    if n % 2 == 0:
        n = n//2
        ans = 'B'+ans
    else:
        n -= 1
        ans = 'A'+ans
print(ans)
