# h, w, n = map(int, input().split())

# two_d_list = [[0 for i in range(w)] for j in range(h)]
# print(two_d_list)
# for i in range(n):
#     a, b = map(int, input().split())
#     two_d_list[a-1][b-1] = i+1
# print(two_d_list)

# # 全て0の配列を削除 0の配列がなくなるまで繰り返す
# while True:
#     try:
#         two_d_list.remove([0 for i in range(w)])
#     except ValueError:
#         break
# print(two_d_list)


# tmp_list = []
# for i in range(len(two_d_list)-1):
#     for j in range(len(two_d_list[i])):
#         if two_d_list[i][j] != 0:
#             tmp_list.append(two_d_list[i][j])


H, W, N = map(int, input().split())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)
print(R)
print(C)

Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
Cs = sorted(set(C))


print(Rs)
print(Cs)

# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
Rd = {x: i for i, x in enumerate(Rs, 1)}
print(Rd)
Cd = {x: i for i, x in enumerate(Cs, 1)}
print(Cd)
for r, c in zip(R, C):
    print(Rd[r], Cd[c])
