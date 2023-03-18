# a,b,c,d=map(int, input().split())
# name_before='Takahashi'
# name_after='Aoki'
# d+=1

# if a==0 and c==23:
#     print(name_before)
# else:
#     if a>b:
#         print(name_after)
#     else:
#         if a==c:
#             print(name_before if a < d else name_after)
#         else:
#             print(name_before)

a,b,c,d=map(int, input().split())
fir=60*a+b
sec=60*c+d
print("Takahashi" if fir<=sec else "Aoki" )