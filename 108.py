# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    	if nums is None:
    		return None
    	begin, end = 0, len(nums) - 1
    	if begin > end:
    		return None
    	mid = (begin + end) >> 1
    	root = TreeNode(nums[root])
    	root.left = self.sortedArrayToBST(nums[begin : mid])
    	root.right = self.sortedArrayToBST(nums[mid+1 : end])
    	return root