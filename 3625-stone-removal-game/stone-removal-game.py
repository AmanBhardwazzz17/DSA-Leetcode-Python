class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_to_remove = 10
        while n >= stones_to_remove:
            n -= stones_to_remove
            stones_to_remove -= 1
        return stones_to_remove % 2 == 1
        