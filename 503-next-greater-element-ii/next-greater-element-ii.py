class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            x = nums[i % n]
            while stack and x > nums[stack[-1]]:
                res[stack.pop()] = x
            if i < n:                         # push sirf pehle round me
                stack.append(i)
        return res
        