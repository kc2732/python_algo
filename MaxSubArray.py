class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = maxSum = nums[0];

        for i in nums[1:]:
            curSum = max(curSum + i, i)
            maxSum = max(curSum, maxSum)

        return maxSum