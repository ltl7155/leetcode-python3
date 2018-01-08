class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] == target:
                return left
            if A[right] == target:
                return right
            m = (left + right) // 2
            mid = A[m]
            if mid == target:
                return m
            if mid > A[left]:
                if A[left]< target and target < A[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if A[m] < target and target < A[right]:
                    left = m + 1
                else:
                    right = m - 1
        else:
            return -1