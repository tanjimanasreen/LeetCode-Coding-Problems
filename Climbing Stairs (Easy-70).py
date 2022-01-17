# Problem Link: https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        count = 1
        sum = 0
        while count <= n:
            sum = first + second
            first = second
            second = sum
            count+=1

        return sum