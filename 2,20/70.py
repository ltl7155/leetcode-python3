class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dis = []
        dis.append(1)
        dis.append(1)

        for i in range(2, n+1):
            dis.append(dis[i-1]+dis[i-2])

        return dis[n]