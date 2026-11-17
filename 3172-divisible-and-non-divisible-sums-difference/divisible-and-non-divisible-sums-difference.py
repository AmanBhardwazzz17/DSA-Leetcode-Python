class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible_sum = sum(x for x in range(1, n + 1) if x % m == 0)
        non_divisible_sum = sum(x for x in range(1, n + 1) if x % m != 0)
        return non_divisible_sum - divisible_sum

        