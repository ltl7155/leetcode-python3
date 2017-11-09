#正则表达式匹配的判断。网上很多的解法是用递归做的，用java和c++都可以过，
# 但同样用python就TLE，说明这道题其实考察的不是递归。而是动态规划，使用动态规划就可以AC了。
# 这里的'*'号表示重复前面的字符，注意是可以重复0次的。
#
# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(p) == 0 and len(s) > 0:
#             return False
#         if len(s) == 0 and len(p) > 0:
#             if len(p) == 2 and p[1] == '*':
#                  return True
#             return False
#         if len(p) >= 2:
#             if p[1] == '*':
#                 if s[0] == p[0] or p[0] == '.':
#                     if not self.isMatch(s[1:], p):
#                         if not self.isMatch(s[1:] , p[2:]):
#                             return self.isMatch(s , p[2:])
#                         return True
#                     else :
#                         return True
#                 else:
#                     return self.isMatch(s, p[2:])
#         if len(s) == 0 and len(p) == 0:
#             return True
#         if s[0] == p[0] or p[0] == '.':
#             return self.isMatch(s[1:], p[1:])
#         return False
#
# s = Solution()
# print (s.isMatch("a",".*a*a"))

#http://blog.csdn.net/gds2014/article/details/50437628
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]

