class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        d = 2
        while d * d <= n:
            while n % d == 0:
                result += d
                n //= d
            d += 1
        if n > 1:
            result += n
        return result