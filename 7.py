class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int_max = 2 ** 31
        int_min = - 2**31 - 1
        s = str(x)
        if s[0] == '-':
            sf = s[1:]
            sb = sf[::-1]
            newS = '-' + sb
        else :
            newS = s[::-1]

        if int(newS) > int_max or int(newS) < int_min:
            return 0
        else:
            return int(newS)

S = Solution()
print (S.reverse(-123))


