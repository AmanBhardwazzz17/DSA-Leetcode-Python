class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        expected = sorted(expected)
        count = 0
        n = len(heights)
        for i in range(n):
            if heights[i] != expected[i]:
                count += 1
        return count 
            


        