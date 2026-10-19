class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n = len(nums)
        low = 0 
        high = n - 1
        while (low <= high):
            mid = low + (high - low)//2
            if nums[mid] == target:
                # Target ke saare indices ki list return karo
                return [i for i in range(n) if nums[i] == target]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1        
        return []

                


        
        