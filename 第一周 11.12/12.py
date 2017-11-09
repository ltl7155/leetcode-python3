# 作者：bluescorpio
# 链接：http://www.jianshu.com/p/15e5ce748c54
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                 ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                 ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                 ["", "M", "MM", "MMM"]]
        res = []
        res.append(roman[3][num // 1000 % 10])
        res.append(roman[2][num // 100 % 10])
        res.append(roman[1][num // 10 % 10])
        res.append(roman[0][num % 10])
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    num = 1
    print (sol.intToRoman(num))
    print (sol.intToRoman(1980))
