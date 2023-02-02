from collections import Counter
mod = 10**9+7


s = input()
t = '*chokudai'
dp = Counter()
# print(dp)
dp['*'] = 1
for char in s:
    if char in t:
        #   ここで、charの前の文字を取得する。
        char_prev = t[t.index(char)-1]
        # print('1', char, char_prev)
        #   ここで、charの前の文字のdpを取得する。文字列を足していく。そして、カウントする。
        dp[char] += dp[char_prev]
        # print('2', dp)
        #   ここで、charのdpを更新する。
        dp[char] %= mod
        # print('3', dp)
print(dp['i'])
