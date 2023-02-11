

# kの進数を10進数に変換する関数
def k_to_10(k, n):
    #   n[::-1]でnを逆順にする
    ans = 0
    #  enumerateでインデックスと要素を取得
    for i, num in enumerate(n[::-1]):
        #   int(num)で文字列を数値に変換
        ans += int(num) * (k**i)
    return ans


k = int(input())
a, b = map(int, input().split())

ans = 1
#  関数を呼ぶ
ans *= k_to_10(k, str(a))
ans *= k_to_10(k, str(b))

print(ans)
