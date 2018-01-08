class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        leftMax = []
        rightMax = []
        result = l = r = 0
        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
            leftMax.append(l)
        for i in range(len(height)-1,-1, -1):
            if height[i] > r:
                r = height[i]
            rightMax.append(r)
        
        rightMax.reverse()
        for i in range(len(height)):
            if leftMax[i]!= 0 and rightMax[i]!=0:
                h = min(leftMax[i],rightMax[i])
                result += h - height[i]
        return result


