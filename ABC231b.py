import collections
n=int(input())
n_list=[]
for _ in range(n):
    n_list.append(input())

# リストの一番出現数が多いものを出力する
c = collections.Counter(n_list)
print(c.most_common()[0][0]) 