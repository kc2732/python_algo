class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = []
        for i in nums:
            if i in dict:
                return True
            else:
                dict.append(i)
        return False

    def containsDuplicateII(self,nums):
        return len(nums) != len(set(nums))