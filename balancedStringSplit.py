class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_L = 0
        cnt_R = 0
        result = 0
        for i in s:
            if i == "L":
                cnt_L += 1
            else:
                cnt_R += 1
            if cnt_L==cnt_R:
                result += 1
                cnt_L = 0
                cnt_R = 0
        return result
                

#정답코드
# def balancedStringSplit(self, s: str) -> int:
#     res = cnt = 0         
#     for c in s:
#         cnt += 1 if c == 'L' else -1            
#         if cnt == 0:
#             res += 1
#     return res  
                
        