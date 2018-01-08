class Solution:
    def uniquePaths(self, m, n):

        map = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
           map[i][0] = 1
        for i in range(n):
            map[0][i] = 1

        for i in range(m-1):
            for j in  range(n-1):
                map[i+1][j+1] = map[i][j+1]+map[i+1][j]
        return map[m-1][n-1]

s =Solution()
s.uniquePaths(2,2)



