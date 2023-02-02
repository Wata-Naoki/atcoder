s = ['H', '2B', '3B', 'HR']

for i in range(4):
    target = input()
    if target in s:
        s.remove(target)

print('Yes' if s == [] else 'No')
