class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import numpy as np
        return np.transpose(matrix)


#정답코드
# class Solution(object):
#     def transpose(self, A):
#         R, C = len(A), len(A[0])
#         ans = [[None] * R for _ in xrange(C)
#         for r, row in enumerate(A):
#             for c, val in enumerate(row):
#                 ans[c][r] = val
#         return ans