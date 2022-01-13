# Problem Link: https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}  # A HashMap to save the number and index

        for i, n in enumerate(nums):
            difference = target - n

            if difference in checker:
                return [checker[difference], i]
            else:
                checker[n] = i
        return

