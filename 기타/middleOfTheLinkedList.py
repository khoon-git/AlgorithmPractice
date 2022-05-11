# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        cnt = 0
        result = ListNode()
        while cur:
            cnt+=1
            cur = cur.next
        cn = cnt / 2
        while cn != 0:
            head = head.next
            cn -= 1
        return head

#정답코드
# class Solution:
#     def middleNode(self, head: ListNode) -> ListNode:
#         arr = [head]
#         while arr[-1].next:
#             arr.append(arr[-1].next)
#         return arr[len(arr) // 2]