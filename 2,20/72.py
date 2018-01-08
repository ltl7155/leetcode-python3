class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = [[0 for i in range(len(word1) + 1)] for j in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dis[0][i] = i
        for j in range(len(word2) + 1):
            dis[j][0] = j

        for i in range(1,len(word2) + 1):
            for j in range(1,len(word1) + 1):
                if word2[i-1] == word1[j-1]:
                    dis[i][j] = dis[i-1][j-1]
                else:
                    dis[i][j] = min(dis[i-1][j-1],dis[i][j-1],dis[i-1][j]) + 1

        return dis[len(word2)][len(word1)]


s = Solution()
s.minDistance("a","b")