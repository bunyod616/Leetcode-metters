class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = ''

        minWord = min(strs)
        maxWord = max(strs)

        i = 0
        N = min(len(minWord), len(maxWord))

        while i < N:
            if minWord[i] == maxWord[i]:
                a += minWord[i]
            else:
                break
            i += 1

        return a


"""

   Longest Common Prefix link:

   https://leetcode.com/problems/longest-common-prefix/

"""