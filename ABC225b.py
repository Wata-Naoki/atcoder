n=int(input())

counter = [0] * (n+1) 
for _ in range(n-1):
    a, b=map(int, input().split())
    counter[a] += 1
    counter[b] += 1
  
print('yes' if n-1 in  counter else 'no')    