s=list(input())
s2=list(input())
print( s,'1')
print( s2,'1')
flag=False

for v, v2 in zip(s, s2):
    print(v, v2)
    if v=='#' and v2=='#':
        flag=True
        break
print('Yes' if flag else 'No')