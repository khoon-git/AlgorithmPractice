class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = -1
        for i in s:
            cnt = t.find(i, cnt+1)
            if cnt == -1: return False
        return True
            
# str.find(찾을 문자, 찾을 위치) -> str안에 찾을 위치부터 끝까지 찾을 문자가 있는지 -> 리턴값은 없으면 -1 있으면 그 위치
# str.startwith(문자) -> "문자"로 시작하는지 return -> bool        
# str.endwith(문자) -> "문자"로 끝나는지 return -> bool
