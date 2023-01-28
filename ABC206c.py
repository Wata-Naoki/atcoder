# import itertools


# import itertools
# n = int(input())
# a_list = [int(v) for v in input().split()]
# count = 0
# for i in range(n):
#     for j in range(n):
#         if a_list[i] != a_list[j] and i < j:
#             count += 1
# print(count)


# n = int(input())
# a_list = [int(v) for v in input().split()]
# all = itertools.combinations(a_list, 2)
# for x in all:
#     print(x)


# 入力の受け取り
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

# defaultdictのインポート
# 要素の出現回数を数える連想配列countを用意
count = defaultdict(int)

# Aのそれぞれの要素(a)について
for a in A:
    # aの出現回数を+1
    count[a] += 1

# 全組み合わせ=N*(N-1)//2
ans = N*(N-1)//2

# countの値(x)それぞれについて
for x in count.values():
    # Ai=Ajとなる組の数x*(x-1)//2を引く
    ans -= x*(x-1)//2

# 答えの出力
print(ans)
