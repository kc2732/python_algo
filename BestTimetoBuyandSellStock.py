class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxint
        prof = 0;
        for i  in prices:
            min_price = min(i, min_price)
            prof = max(prof, i-min_price)
        return prof