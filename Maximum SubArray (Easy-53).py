# Problem Link: https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0

            currentSum = currentSum + n
            maxSum = max(currentSum, maxSum)

        return maxSum


