class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = float ('-inf')
        while (low <= high ):
            mid = low + (high - low)//2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans

            



        
       