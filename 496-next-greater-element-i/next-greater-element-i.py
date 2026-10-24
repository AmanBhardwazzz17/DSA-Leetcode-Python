class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_map = {}
        stack = []
        # agle bade sambandhon ko map karne ke liye nums2 ko process karna hai
        for num in nums2:
            # jab tak stack mein tatv maujood hain aur vartmaan sankhya, 
            # stack ke sheersh par maujood tatv se badi hai
            while stack and num > stack[-1]:
                popped_element = stack.pop()
                next_greater_map[popped_element] = num
            stack.append(num)
        # map ka upyog karke nums1 ke liye antim uttar suchi banaen
        # yadi koi sankhya map mein maujood nahin hai, to uska agla bada tatv -1 hai
        return [next_greater_map.get(num, -1) for num in nums1]

        