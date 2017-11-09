# 注意一下算法：
# 对于输入的罗马数字字符串，从后向前扫描，
# 遇到前面数大于等于后面的最大数的时候，相加；遇到前面数小于后面的最大数的时候，相减。

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sum = 0
        for i in range(0, len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                sum = sum - d[s[i]]
            else:
                sum = sum + d[s[i]]
        sum = sum + d[s[-1]]
        return sum