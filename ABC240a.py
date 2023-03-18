a, b=map(int, input().split())
diff=abs(a-b)

if diff==9 :
    print('Yes')
else:
    if abs(a-b)==1:
        print('Yes')
    else:
        print('No')
