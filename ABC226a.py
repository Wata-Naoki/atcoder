
# これだとWA。0.5が0になり偶数の方にまるめられてしまう
# x=float(input())
# # xを小数第１位を四捨五入する
# print(round(x))


# 完全に四捨五入する
# from decimal import Decimal, ROUND_HALF_UP
# n_str = input()
# result = Decimal( n_str ).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
# print(result)


a, b=map(int, input().split('.'))
ans = a
if  b >= 500:
    ans += 1
print(ans)
