

n=int(input())
dic={}

for _ in range(n):
    a, b=map(int, input().split())
    dic[a]=b
print(dic)