# 贪心算法


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        reach = nums[0]
        for i in range(1, len(nums)):
            if reach >= i:
                if i + nums[i] > reach:
                    reach = i+nums[i]
            if reach>=len(nums)-1:
                return True
        return False

s = Solution()
s.canJump([2,5,0,0])