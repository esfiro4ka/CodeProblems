class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                t += i
        for i in range(0, len(t)):
            if t[i] != t[-i-1]:
                return False
        return True