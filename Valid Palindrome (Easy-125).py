# Problem Link: https://leetcode.com/problems/valid-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = "".join(c for c in s if c.isalnum()).lower()
        s_reverse = s_new[::-1].lower()

        if s_new == s_reverse:
            return True
        else:
            return False