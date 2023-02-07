import math
x = input()
int_x = math.floor(float(x))
if 0 <= int(x[-1]) <= 2:
    print(str(int_x) + '-')
elif 3 <= int(x[-1]) <= 6:
    print(str(int_x))
elif 7 <= int(x[-1]) <= 9:
    print(str(int_x) + '+')
