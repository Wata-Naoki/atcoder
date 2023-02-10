x = input()

dict = {}
for i in range(len(x)):
    dict[x[i]] = i

# {'b': 0, 'a': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'z': 24, 'y': 25}
# print(dict)

n = int(input())
names = []
for _ in range(n):
    name = input()
    new_order = []
    for n in name:
        new_order.append(dict[n])
    names.append([new_order, name])


# [[[1, 0, 23], 'abx'], [[0, 24, 24], 'bzz'], [[0, 24, 25], 'bzy'], [[2, 1, 1], 'caa']]
# print(names)

names.sort()
# [[[0, 24, 24], 'bzz'], [[0, 24, 25], 'bzy'], [[1, 0, 23], 'abx'], [[2, 1, 1], 'caa']]
# print(names)
for name in names:
    print(name[1])
    # bzz bzy abx caa
