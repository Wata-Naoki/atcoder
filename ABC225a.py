s = input()

# sの組み合わせ
n=len(set(s))

if n==1:
    print(1)
elif n==2:
    print(3)
else:
    print(6)