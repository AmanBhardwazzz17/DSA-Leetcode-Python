class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        # nums2 ke element ka next greater store karenge
        next_greater_map = {}
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if not stack:
                next_greater_map[nums2[i]] = -1
            else:
                next_greater_map[nums2[i]] = stack[-1]
            
            stack.append(nums2[i])
        # Ab nums1 ka answer map se nikalo
        ans = []
        for num in nums1:
            ans.append(next_greater_map[num])    
        return ans