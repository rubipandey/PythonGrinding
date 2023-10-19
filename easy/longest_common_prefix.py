"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

Link:
https://leetcode.com/problems/longest-common-prefix/submissions/1071528062/
"""

from typing import List
import copy
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens = [len(i) for i in strs]
        if len(strs)==1:
            return strs[0]
        str_copy = copy.deepcopy(strs)
        min_len = min(lens)
        idx_min = lens.index(min_len)
        str_copy.remove(str_copy[idx_min])
        count_chr = []
        for i in range(min_len):
            count1 = 0
            for j in str_copy:
                if strs[idx_min][i] == j[i]:
                    count1 = count1+1
            if count1==len(str_copy):
                count_chr.append(strs[idx_min][i])
                continue
            else:
                break
        return ''.join(count_chr)

object_solution = Solution()
#fl ==> Intented output

print(object_solution.longestCommonPrefix(["flower","flow","flight"]))