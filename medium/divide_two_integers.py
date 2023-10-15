"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Problem link:
https://leetcode.com/problems/divide-two-integers/submissions/1071546105/
"""
import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = dividend/divisor
        if q >= 2**31:
            return(2**31-1)
        elif q>0:
            return math.floor(q)
        else:
            return math.ceil(q)


object_solution = Solution()
# -2 ==> Intented output
print(object_solution.divide(7,-3))