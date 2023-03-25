a, b, k = map(int, input().split())

tmp_a = a
count = 0
while tmp_a < b:
    tmp_a *= k
    count += 1
print(count)
