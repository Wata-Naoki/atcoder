
class Solution:
    def claimStairs(self, n: int):
        if n<=1:
            return n
        num1, num2 = 0, 1
        for i in range(n):
            num1, num2 = num2, num1+num2
        return num2
    
n=int(input())
print(Solution().claimStairs(n))