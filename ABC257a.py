n, x = map(int, input().split())
alp = [chr(i).upper() for i in range(97, 123)]
chars = "".join(alp)
# print(chars)
txt = ""
for char in chars:
    txt += char * n
print(txt[x - 1])

# アルファベットをaからzまで生成し、文字列alpに格納
# alp = [chr(i) for i in range(97, 123)]
# # 文字列にして表示
# st_alp = "".join(alp)
# print(st_alp)
