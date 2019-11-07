class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    	"""
    	Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        Output: [1,2,2,3,5,6]

    	"""
    	nums1_copy = nums1[:m]
    	nums1[:] = []
    	p1, p2 = 0, 0
    	while p1 < m and p2 < n:
    		if nums1_copy[p1] < nums2[p2]:
    			nums1.append(nums1_copy[p1])
    			p1 += 1
    		else:
    			nums2.append(nums2[p2])
    			p2 += 1

    	if p2 < n:
    		nums1[p1 + p2 :] = nums2[p2:]
    	if p1 < m:
    		nums1[p1 + p2 :] = nums1_copy[p1:]