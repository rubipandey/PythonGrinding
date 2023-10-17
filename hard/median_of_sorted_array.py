"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Link:
https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/588066433/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        len_array = len(nums1)
        if len_array % 2 == 0:
            quo = len_array // 2
            num = (nums1[quo - 1] + nums1[quo]) / 2
        elif len_array == 1:
            num = nums1[0]
        else:
            ind = (len_array + 1) // 2
            num = nums1[ind - 1]
        return (num)

object_solution = Solution()
# 2.5==> Intented output
print(object_solution.findMedianSortedArrays([1,2],[3,4]))