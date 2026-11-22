class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_sum = n * n
        even_sum = n * (n + 1)
        import math
        return math.gcd(odd_sum, even_sum)
        