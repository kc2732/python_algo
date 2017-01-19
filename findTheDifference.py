class Solution:
    def findTheDifference(self,s,t):
        res = 0;
        tmp = s+t
        for ch in tmp:
            res ^= ord(ch)
        return chr(res)