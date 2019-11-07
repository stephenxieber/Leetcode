class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
    	size = len(nums)
    	if size == 0: return 0
    	left, right = 0, size
    	while left < right:
    		mid = left + (right - left) // 2
    		if target > nums[mid]:
    			left = mid + 1
    		else:
    			assert target <= nums[mid]
    			right = mid 
    	return left