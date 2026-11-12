class Solution:
    def isHappy(self, n: int) -> bool:
        # Yeh function linked list ke '.next' ki tarah kaam karega
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total += digit ** 2
            return total
        slow = fast = n
        while fast != 1 and get_next(fast) != 1:
            slow = get_next(slow)               # slow = slow.next
            fast = get_next(get_next(fast))     # fast = fast.next.next
            if fast == slow:                    # agar fast == slow -> cycle hai
                return False        
        return True


        