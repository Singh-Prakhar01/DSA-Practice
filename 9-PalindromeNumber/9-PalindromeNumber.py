# Last updated: 27/07/2026, 15:21:04
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        res = a[::-1] 
        
        if a == res :
            return True
        else :
            return False