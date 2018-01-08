# 这个题必须要原地删除重复元素

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        num = 0
        index = 0
        for i in nums[1:]:
            if i != nums[index]:
                index += 1
                nums[index] = i

        return index + 1

s= Solution()
s.removeDuplicates([1,1,2])