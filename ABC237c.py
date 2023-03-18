
def judge():
    s=input()
    l = len(s) - len(s.lstrip('a'))
    r = len(s) - len(s.rstrip('a'))
    if l > r: return False
    ans  = 'a' * (r-l) + s
    return ans==ans[::-1]

print('Yes' if judge() else 'No')
