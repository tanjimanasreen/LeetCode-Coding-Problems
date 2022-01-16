# Problem Link: https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))

        if s_list == t_list:
            return True
        else:
            return False