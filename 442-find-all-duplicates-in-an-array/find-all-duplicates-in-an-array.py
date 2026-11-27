class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        duplicates = []
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates