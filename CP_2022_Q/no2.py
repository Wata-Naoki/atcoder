# 入力で縦と横n個のデータが入ってくるので、それをリスト化して、それぞれの要素を比較していく。重複があればinvalid。なければvalidと出力する。
input_list = [a for a in input().split() for _ in range(3)]
print(input_list)

# 入力で縦と横n個のデータを受け取る
input_list