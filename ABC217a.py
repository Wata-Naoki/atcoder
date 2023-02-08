# 入力を受け取る
S, T = map(str, input().split())
# もし辞書順でS<Tならば
if S < T:
    # Yesを出力
    print("Yes")
# そうでないならば(辞書順でT<Sならば)
else:
    # Noを出力
    print("No")
