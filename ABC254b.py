n = int(input())
ans = [[0] * (i + 1) for i in range(n)]
# print(ans)
for i in range(n):
    for j in range(i + 1):
        # 行の最初と最後の値は1にする
        if j == 0 or j == i:
            ans[i][j] = 1
        else:
            # 最初と最後以外は、1つ前の行の1つ前の順番の値と今の順番の値
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]

for i in range(n):
    print(*ans[i])
