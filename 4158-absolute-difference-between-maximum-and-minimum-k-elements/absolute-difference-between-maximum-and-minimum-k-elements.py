class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[:k]) - sum(nums[-k:])) if k else 0
        