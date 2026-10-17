from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digit_sum(num):
            return sum(int(digit) for digit in str(num))

        n = len(nums)

        # 1. Digit Sum ke according sort karo
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # 2. Har element ka target index
        pos = {val: idx for idx, val in enumerate(sorted_nums)}
        target_index = [pos[val] for val in nums]

        # 3. Cycle counting
        visited = [False] * n
        total_swaps = 0

        for i in range(n):
            if not visited[i]:
                curr = i
                count = 0

                while not visited[curr]:
                    visited[curr] = True
                    curr = target_index[curr]
                    count += 1

                if count > 1:
                    total_swaps += count - 1

        return total_swaps