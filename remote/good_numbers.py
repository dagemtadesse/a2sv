import math

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def modp(base, pow, m):
            if pow == 0:
                return 1 
            sol = modp(base, pow // 2, m)
            if pow % 2 == 1:
                return sol * sol * base % m
            else:
                return sol * sol % m

        odds = n // 2
        evens = n // 2 + n % 2

        m = 10**9+7
        return (modp(5, evens, m) * modp(4, odds, m)) % m

   
