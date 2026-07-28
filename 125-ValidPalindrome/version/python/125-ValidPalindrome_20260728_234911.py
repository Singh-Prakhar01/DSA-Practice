# Last updated: 28/07/2026, 23:49:11
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        temp = ""
4
5        for ch in s:
6            if ch.isalnum():
7                temp += ch.lower()
8
9        return temp == temp[::-1]