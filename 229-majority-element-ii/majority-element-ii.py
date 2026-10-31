class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        # 1. Pehle array ko sort kiya taaki same numbers ek sath aa jayein
        nums.sort()
        ans = []
        n = len(nums)
        threshold = n // 3
        # 2. Pure array me elements aur unke count ko track karenge
        current_element = None
        current_count = 0
        for num in nums:
            if num == current_element:
                current_count += 1
            else:
                # Naya element milte hi purane wale ka check khatam
                current_element = num
                current_count = 1    
            # 3. Agar count exact threshold + 1 ho jaye, toh winner mil gaya
            # (Duplicate entry se bachne ke liye '==' check sabse best hai)
            if current_count == threshold + 1:
                ans.append(current_element)        
        return ans



        