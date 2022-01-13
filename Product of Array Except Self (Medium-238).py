# Problem Link: https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        l = len(nums)

        product = 1
        result.insert(0, product)
        for i in range(1, l):
            product = product * nums[i-1]
            result.insert(i, product)

        product = 1
        for i in range(len(nums)-2, -1, -1):
            product = product * nums[i+1]
            result[i] = result[i] * product

        return result
