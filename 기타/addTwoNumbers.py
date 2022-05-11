# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = 1
        carry = 0
        sum = 0
        while l1 or l2:
            if carry == 0 and l1 and l2:
                if (l1.val + l2.val) >= 10:
                    carry = 1
                    sum += ((l1.val + l2.val) % 10) * cur
                else:
                    carry = 0
                    sum += ((l1.val + l2.val) % 10) * cur
            elif carry == 1 and l1 and l2:
                if (l1.val + l2.val) + 1 >= 10:
                    carry = 1
                    sum += (((l1.val + l2.val) + 1) % 10) * cur
                else:
                    carry = 0
                    sum += (((l1.val + l2.val) + 1)% 10) * cur
            else:
                if carry == 0 and l1:
                    sum += l1*cur
                elif carry == 1 and l1:
                    if carry+l1.val >= 10:
                        carry = 1
                        sum += ((l1.val+1) % 10) * cur
                        print(carry+l1.val)
                        print("test21")
                    else:
                        print(carry+l1.val)
                        carry = 0
                        sum += ((l1.val+1) % 10) * cur
                        print("test3")
                elif carry == 0 and l2:
                    sum += l1*cur
                elif carry == 1 and l2:
                    if carry+l2.val >= 10:
                        carry = 1
                        sum += ((l2.val+1) % 10) * cur
                        print("test2")
                    else:
                        carry = 0
                        sum += ((l2.val+1) % 10) * cur
                        print("test4")
            cur *= 10
            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            elif l1:
                l1 = l1.next
            else:
                l2 = l2.next
            print(sum)
        result = reversed(str(sum))
        cur = ListNode()
        head = None
        for i in result:
            if not head:
                head = ListNode(int(i))
                cur = head
            else:
                cur.next = ListNode(int(i))
                cur = cur.next 
        return head

# 정답코드
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         head = ListNode()
#         result = head
#         carry = 0
#         while (l1 or l2 or carry):
#             if l1 and l2 드
#                 carry = (result.val + l1.val + l2.val) // 10
#                 sum = result.val + l1.val + l2.val - (carry*10)
#                 result.val = sum
#             elif l1 or l2 :
#                 c = l1 if l1 else l2
#                 carry = (result.val + c.val) // 10
#                 sum = result.val + c.val - (carry*10)
#             elif carry :
#                 sum = carry
#                 carry = 0
                
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#             result.val = sum
#             if l1 or l2 or carry :
#                 result.next = ListNode(carry)
#             else : result.next = None
#             result = result.next

#         return head