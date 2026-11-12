class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        Aman = 1
        Ashish = 1
        best = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                Aman += 1
                Ashish = 1
            elif nums[i] < nums[i-1]:
                Ashish += 1
                Aman = 1
            else:
                Aman = 1
                Ashish = 1
            best = max(best,Aman,Ashish)
        return best
        