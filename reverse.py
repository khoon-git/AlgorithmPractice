class Solution(object):
    def reverse(self, x):
        if x > 0:
            value=int(str(x)[::-1])
        else:
            value=-1*int(str(x*-1)[::-1])
        
        if value > 2**31 or value < -2**31:
            value = 0
        return value