s = input()
t = input()

count = 0
for i in range(len(s)-1):
    if s[i] != t[i]:
        count += 1
    if count >= 2:
        break
print('No' if count >= 2 else 'Yes')
