r, c = map(int, input().split())
dis = max(abs(r - 8), abs(c - 8))
print("white" if dis % 2 == 0 else "black")
