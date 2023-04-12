y = int(input())

for i in range(1000):
    new_year = y + i
    if new_year % 4 == 2:
        print(new_year)
        break
