class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        res = []
        length=len(nums)
        if length<3:return res
        nums.sort()
        for i in range(length):
            if nums[i]>0:break
            if i>0 and nums[i]==nums[i-1]:continue
            begin=i+1;end=length-1
            while begin < end:
                sum=nums[i]+nums[begin]+nums[end]
                if sum==0:
                    tmp=[nums[i],nums[begin],nums[end]]
                    res.append(tmp)
                    begin+=1;end-=1
                    while begin<end and nums[begin]==nums[begin-1]:begin+=1
                    while begin<end and nums[end] == nums[end+1]:end-=1
                elif sum>0:end-=1
                else:begin+=1
        return res



s = Solution()
print (s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))