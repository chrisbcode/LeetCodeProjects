# Written by Chris B
# LeetCode TwoSum submission

class Solution(object):
    def twoSum(self, nums, target):
        indices = list()
        for j in range(len(nums)):

            for i in range(j+1,len(nums)):
                if nums[i] + nums[j] == target:
                        indices.append(j)
                        indices.append(i)
                        return indices

        return indices
        
