# 一定要注意append到result的时候是sublist的一个复制品，不然到最后都是空的[]

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.findS(nums,[])
        return self.result

    def findS(self, nums, sublist):
        if len(nums) == len(sublist):
            self.result.append(sublist[:])
            return
        for i in nums:
            if i in sublist:
                continue
            sublist.append(i)
            self.findS(nums, sublist)
            sublist.remove(i)



s = Solution()
s.permute([1,2,3])