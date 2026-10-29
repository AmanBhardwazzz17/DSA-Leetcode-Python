class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        right = 0 
        n = len(nums)
        ans = 0
        sum = 0
        while right < n:
            sum += nums[right]
            while sum >= target and left <= right:
                if ans == 0:
                    ans = right - left + 1
                else:
                    ans = min(ans,right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return ans

                



        

        
        
        