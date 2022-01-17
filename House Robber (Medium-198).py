# Problem Link: https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        opt1 = 0
        opt2 = 0

        for n in nums:
            maxRob = max(opt1 + n, opt2)
            opt1 = opt2
            opt2 = maxRob

        return maxRob