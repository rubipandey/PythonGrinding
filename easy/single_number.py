"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

Link:
https://leetcode.com/problems/single-number/submissions/1068050317/
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            count_i = nums.count(i)
            if count_i==1:
                return(i)

object_solution = Solution()
#4 ==> Intented output
print(object_solution.singleNumber([4,1,2,1,2]))