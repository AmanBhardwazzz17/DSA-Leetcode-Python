class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Har month se pehle tak ke total days ki pre-calculated list
        months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        #MM DD ko day of year me convert karne ka short function
        f = lambda s: months[int(s[:2]) - 1] + int(s[3:])
        
        # Ek hi line me Overlap calculate karke return kar diya
        return max(0, min(f(leaveAlice), f(leaveBob)) - max(f(arriveAlice), f(arriveBob)) + 1)
