#由于python的语言特性，不用建立二维数组，一个数组每个元素都是字符串

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = ["" for _ in range(numRows)]
        print (type(l[0]))
        p = 2 *numRows - 2
        if numRows == 1:
            return s
        for i in range(len(s)):
            k = i % p
            if  k >= numRows :
                l[p - k]+=(s[i])
            else:
                l[k]+=(s[i])
        return "".join(l)


print ("a",5)