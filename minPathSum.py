class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0: return 0;

        dp = [[1 for i in xrange(m)] for j in xrange(n)]

        for x in range(1, m):
            for y in range(1, n):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[n - 1][m - 1]