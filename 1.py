class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index
        for index, num in enumerate(nums):
            result = target - num
            j = hashmap.get(result)
            if j is not None and j != index:
                return [index,j]