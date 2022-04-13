class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def S(i):
            if i == 1: return 1
            if i == 2: return 2
            
            if i not in memo:
                memo[i] = S(i - 1) + S(i - 2)
            return memo[i]
        return S(n)
