
def cal1(t):
    val=t**2+2*t+3
    return val

def cal2(t):
    val=cal1(t)+t
    return val

def cal3(t):
    val=cal1(cal2(t))
    return val

def cal4(t):
    val=cal1(cal1(t))
    return val

def solve(t):
    val =cal1((cal3(t))+cal4(t))
    return val

t=int(input())
print(solve(t))

