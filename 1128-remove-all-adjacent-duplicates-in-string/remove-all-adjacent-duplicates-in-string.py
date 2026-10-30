class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for num in s:
            #Decide when to push or pop
            if stack and stack[-1] == num:
                stack.pop() # Agar match hua to duplicate remove karein
            else:
                stack.append(num) # Agar match nahi hua to push karein        
        # List ko wapas string mein convert karke return karein
        return "".join(stack)

         
        