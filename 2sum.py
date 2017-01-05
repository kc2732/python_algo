class Solution(object):
    def twoSum(self,nums,target):
        buff_dict = {};
        for i in range(len(nums)):
            if nums[i] not in buff_dict:
                buff_dict[target-nums[i]] = i;
            else:
                return [buff_dict[nums[i]],i]