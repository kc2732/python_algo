class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        :This version has a bad time complexity
        """
        n = len(s)
        if n <= 1: return n;
        max_len = 0
        diff = 0;
        for i in range(n - 1):
            Set = set()
            for j in range(i, n):
                if s[j] not in Set:
                    Set.add(s[j])
                    diff = j - i + 1
                    if max_len < diff:
                        max_len = diff
                else:
                    break
        return max_len

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        :This version has a bad time complexity
        """
        n = len(s)
        if n <= 1: return n;
        max_len = 0
        diff = 0;
        for i in range(n - 1):
            Set = set()
            for j in range(i, n):
                if s[j] not in Set:
                    Set.add(s[j])
                    diff = j - i + 1
                    if max_len < diff:
                        max_len = diff
                else:
                    break
        return max_len