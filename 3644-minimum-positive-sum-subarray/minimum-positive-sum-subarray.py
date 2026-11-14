class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        best = float('inf')
        for k in range(l, min(r, n) + 1):       # har length try karo
            window = sum(nums[:k])              # pehli window
            if window > 0:
                best = min(best, window)
            for i in range(k, n):               # window slide karo
                window += nums[i] - nums[i - k]
                if window > 0:
                    best = min(best, window)
        return -1 if best == float('inf') else best
        