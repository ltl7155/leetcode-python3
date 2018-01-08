# 将final = []写在class Solution:下面那行在leetcode里会报错
# 要把它写在方法里面，self.final=[]
class Solution:

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.final = []
        candidates.sort()
        candidates.reverse()

        self.findCom([],candidates, target)

        return (self.final)


    def findCom(self, com, candidates, target):
        thisCom = com.copy()
        if candidates == []:
            return

        if target - candidates[0] > 0:
            thisCom.append(candidates[0])
            self.findCom(thisCom, candidates, target - candidates[0])
        thisCom = com.copy()
        if target - candidates[0] == 0:
            thisCom.append(candidates[0])
            self.final.append(thisCom)
        thisCom = com.copy()
        self.findCom(thisCom, candidates[1:], target)

s = Solution()
s.combinationSum([2],1)