#需要分奇数和偶数长的字符串讨论
#不能用if ，else连接两种情况讨论，比如"ccc"时，在遍历到中间的c时，第一种判断该字符前面是不是c，如果是的话，直接跳过前后都是c是不对的

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 1
        maxStr = s[0 : 1]
        for i in range(1, len(s)) :
            if s[i] == s[i - 1]:
                for j in range(i):
                    if i + j < len(s) and s[i + j] == s[i - 1 - j]:
                        if maxLen < 2 * j + 2:
                            maxLen = 2 * j + 2
                            maxStr = s[i - 1 - j : i + j + 1]
                    else :
                        break

            for j in range(i + 1):
                if i + j < len(s) and s[i + j] == s[i - j]:
                    if maxLen < 2 * j + 1:
                        maxLen = 2 * j + 1
                        maxStr = s[i - j: i + j + 1]
                else :
                    break
        return maxStr


if __name__ == "__main__":
    s = Solution()
    print (s.longestPalindrome("ccc"))
