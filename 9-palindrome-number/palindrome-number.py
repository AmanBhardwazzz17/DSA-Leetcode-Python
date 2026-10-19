class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Number ko string mein convert karke reverse karo
        reverse = str(x)[::-1]
        #Original aur reversed value compare karo
        if str(x) == reverse:
            #True ya False return karo
            return True
        else:
            return False

        