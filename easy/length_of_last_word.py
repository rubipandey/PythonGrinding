"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring  consisting of non-space characters only.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

link:
https://leetcode.com/problems/length-of-last-word/submissions/1071548140/

"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

object_solution = Solution()
#5 ==> Intented output
print(object_solution.lengthOfLastWord(s = "Hello World"))