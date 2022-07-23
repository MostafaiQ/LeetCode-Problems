class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ("".join(filter(str.isalnum,s))).lower()
        for i in range(len(s)):
            if s[i] == s[-1-i]:
                pass
            else:
                return False
        return True