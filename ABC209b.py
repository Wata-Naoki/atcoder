

n, x = map(int, input().split())

# リスト受け取る。偶数番目の要素は-1する。
a_list = list(map(int, input().split()))
#  一番最初の要素はそのままで、偶数番目の要素は-1する。、2個目の
a_list[1::2] = [a - 1 for a in a_list[1::2]]
print('Yes' if sum(a_list) <= x else 'No')
