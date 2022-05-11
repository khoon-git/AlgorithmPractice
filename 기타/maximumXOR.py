class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        i = 0
        j = 0
        while i <= len(nums):
            j = i + 1
            while j <= len(nums):
                r = nums[i]^nums[j]
                print(r)
                if max < r:
                    max = r
                j += 1
            i += 1
        return max

#정답코드
# 
# class Solution:
#     def findMaximumXOR(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         mx,mask=0,0
#         for i in range(31,-1,-1):
#             possible_mx = mx | 1 << i
#             mask = mask | 1 << i
#             bits=set()
#             for num in nums:
#                 bits.add(num & mask)
#             for bit in bits:
#                 if bit ^ possible_mx in bits:
#                     mx = possible_mx
#                     break
#         return mx