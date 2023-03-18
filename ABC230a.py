n=int(input())

if 42 <= n:
    n+=1

n=str(n)

if len(n) >=3:
    print('AGC{}'.format(n) )
elif len(n) >=2:
    print('AGC0{}'.format(n) )
else:
     print('AGC00{}'.format(n) )
