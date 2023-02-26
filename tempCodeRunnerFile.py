<<<<<<< HEAD
n=int(input())
import collections
n_list=[]
for _ in range(n):
    n_list.append(input())

# リストの一番出現数が多いものを出力する
c = collections.Counter(n_list)
print(c.most_common()[0][0])
=======


n=int(input())
dic={}

for _ in range(n):
    a, b=map(int, input().split())
    dic[a]=b
print(dic)
>>>>>>> c2017b84a879745cb3e8bd1b8c2b5e1ede138226
