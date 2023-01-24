
sq_data = []
text_name = input()
with open(text_name) as text_value:
    for line in text_value:
        line = line.rstrip()  # 読み込んだ行の末尾には改行文字があるので削除
        sq_data.append(line.split())  # 空白で区切るため


# flagでもし重複があればその地点でinvalid。trueにして処理を終了。
flag = False
# 横の並びがリスト化されている。その長さとsetで重複したデータを削除できるので、それと比較。変わってたら重複ありということで、その時点でinvalidで終了。
for i, v in enumerate(sq_data):
    if len(v) != len(set(v)):
        flag = True
        break
# 今回は3×3なので、縦の列で重複ないか探すにはzipで取り出すのが簡単。値が同じのがあったらその時点でinvalid。
for fir, sec, thi in zip(sq_data[0], sq_data[1], sq_data[2]):
    if fir != sec != thi:
        continue
    else:
        flag = True
        break

print('invalid' if flag else 'valid')


# 入力で縦と横n個のデータが入ってくるので、それをリスト化して、それぞれの要素を比較していく。重複があればinvalid。なければvalidと出力する。
