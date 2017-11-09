class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre = ""
        flag = True
        if len(strs) == 0:
            return pre
        pre = strs[0]
        for i in range(1, len(strs)):
            for j in range(0, len(pre)):
                if j == len(strs[i]):
                    pre = pre[:j]
                    break
                elif strs[i][j] != pre[j]:
                    pre = pre[:j]
                    break
        return pre
s = Solution()
print (s.longestCommonPrefix(["abab","aba",""]))

