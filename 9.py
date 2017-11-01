class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 :
            return False
        else :
            if self.rev(x) == x:
                return True
            else :
                return False

    def rev(self, x):
        sum = 0
        while x >= 1 :
            sum = sum * 10 + x%10
            x = x//10
        return sum