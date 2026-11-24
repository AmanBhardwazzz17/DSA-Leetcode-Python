import math
from typing import List
class Solution:
  def maxLength(self, nums: List[int]) -> int:
    ans = 2  # Length 2 hamesha valid hoti hai
    left = 0
    prod = 1
    for right, num in enumerate(nums):
      # Jab tak naya number purane numbers ke saath factor share kare, window chhoti karein
      while math.gcd(prod, num) != 1:
        prod //= nums[left]
        left += 1
      prod *= num
      ans = max(ans, right - left + 1)
    return ans

        