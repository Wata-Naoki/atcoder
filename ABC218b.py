
p = [int(x) for x in input().split()]
# アルファベットのリストを作成
alphabet = [chr(i) for i in range(97, 97+26)]
# print(alphabet)
ans = ''
for val in p:
    ans += alphabet[val-1]
print(ans)
