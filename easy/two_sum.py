"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Problem link :
https://leetcode.com/problems/two-sum/description/
"""
from typing import List
class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums:
                try:
                    return [i, nums.index(remain, i+1)]
                except:
                    continue

object_solution = Solution()
# [0,1] ==> Intented output
print(object_solution.twosum([2,7,11,15],9))