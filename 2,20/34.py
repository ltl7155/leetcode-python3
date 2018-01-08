class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left, right = 0, len(nums)-1
        return self.binSearch(left, right, nums, target)


    def binSearch(self, left, right, nums, target):
        if left > right:
            return [-1, -1]
        l = []
        r = []
        mid = (left + right)//2
        if target == nums[mid]:
            l = self.binSearch(left, mid - 1, nums, target)
            r = self.binSearch(mid + 1, right, nums, target)
            if  l[0] == -1:
                l[0] = mid

            if r[0] == -1:
                r[1] = mid
                r[1] = mid
            return [l[0], r[1]]
        else:
            l = self.binSearch(left, mid - 1, nums, target)
            r = self.binSearch(mid + 1, right, nums,target)
            if l[0] == -1:
                if r[0] == -1:
                    return [-1, -1]
                else:
                    return r
            else:
                return l

H = [5,7,7,8,8,10]
S = Solution()
print (S.searchRange(H, 8))
