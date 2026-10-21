class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_product = 1
        digit_sum = 0
        while n != 0:
            digit = n % 10
            digit_product *= digit  
            digit_sum += digit 
            n = n // 10
        return digit_product - digit_sum



        
        