class Solution:
    def countDigits(self, num: int) -> int:
        Aman_num = num
        count = 0
        while num!= 0:
            digit = num % 10
            if Aman_num % digit == 0:
                count += 1
            num = num//10
        return count 

        