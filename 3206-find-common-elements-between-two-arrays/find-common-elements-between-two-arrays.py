class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans1 = 0
        for x in nums1:
            if x in set2:
                ans1 += 1        
        ans2 = 0
        for x in nums2:
            if x in set1:
                ans2 += 1        
        return [ans1, ans2]

        