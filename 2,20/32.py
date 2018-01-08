class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        last = -1
        stack = []
        if s == "":
            return 0
        k = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack == []:
                    last = i
                    k = 0
                else:
                    stack.pop()
                    k += 2
                    if stack == []:
                        m = max(m, k)
                    else:
                        m = max(m, i -stack[len(stack) -1])
        return m

S = Solution()
print (S.longestValidParentheses("()()"))

