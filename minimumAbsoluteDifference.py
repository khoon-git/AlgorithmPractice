# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def fn(node, lo, hi):
            if not node: return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))


#min(a, b, args*) -> a, b 들어오는 모든 반복가능한 자료형들 중 가장 작은 값
#max(a, b, args*) -> a, b 들어오는 모든 반복가능한 자료형들 중 가장 큰 값
#zip 함수 예제로 이해하기 -> 집을 지어서 만들어서 내보낸다.
# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]
# for pair in zip(numbers, letters):
# ...     print(pair)
# ...
# (1, 'A')
# (2, 'B')
# (3, 'C')