# 一直没做对

# 不能乘除就加减就行了，但是一个问题是加减有可能速度太慢，因此需要转换，
# 由于任何一个数都能表示成二进制，所以有dividend=divisor*（a*2^1 + b*2^2 + ...... + m*2^k）
# 所以只要计算出所有divisor*2^k，然后减去即可。
# 将一个数左移等于将一个数×2，取一个tmp = divisor，所以将除数tmp不断左移，直到其大于被除数dividend，
# 然后得到dividend - tmp，重复这个过程。

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                quotient += 1 << k
                tmp <<= 1
                k += 1
        quotient  = sign * quotient
        if quotient > MAX_INT:
            quotient = MAX_INT
        return quotient