# Problem Link: https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        if len(set_nums) != len(nums):
            return True
        else:
            return False