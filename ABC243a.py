v, a, b,c=map(int, input().split())

while True:
    if v-a<0:
        print('F')
        break
    v-=a
    if v-(b) <0:
        print('M')
        break
    v-=b
    if v-c <0:
        print('T')
        break
    v-=c
    



# if v-a<=0:
#     print('F')
# elif v-(a+b) <=0:
#     print('M')
# elif v-(a+b+c) <=0:
#     print('T')