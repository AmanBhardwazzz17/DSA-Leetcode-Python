class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        mpp = {}
        threshold = len(nums) // 2
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1
            if mpp[num] > threshold:
                return num


        
        