"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Link:
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/1068011502/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            indx = haystack.index(needle)
            return(indx)
        except:
            return(-1)

object_solution = Solution()
#0 ==> Intented output
print(object_solution.strStr(haystack = "sadbutsad", needle = "sad"))