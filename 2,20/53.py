class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        maximum = []
        startPos = []
        for i in range(l):
            if i == 0:
                maximum.append(nums[0])
                startPos.append(0)
            else:
                if maximum[i-1] <= 0:
                    maximum.append(nums[i])
                    startPos.append(i)
                else:
                    maximum.append(maximum[i-1] + nums[i])
                    startPos.append(startPos[i-1])
        tempMax = 0
        for i in range(l):
            if maximum[tempMax] < maximum[i]:
                tempMax = i

        print (nums[startPos[tempMax]:tempMax+1])


s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

