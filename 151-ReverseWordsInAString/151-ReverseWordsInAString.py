# Last updated: 27/07/2026, 15:21:08
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        s.reverse()
        s = " ".join(s)

        return s