# 首先以从对角线为轴翻转，然后再以x轴中线上下翻转即可得到结果，如下图所示(其中蓝色数字表示翻转轴)：

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0]) - 1
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n-j][n-i] = matrix[n-j][n-i], matrix[i][j]

        for i in range(n + 1):
            if(i < (n+1)//2):
                for j in range(n + 1):
                    matrix[i][j],matrix[n - i][j] = matrix[n - i][j],matrix[i][j]



