class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    	sum = 0
    	for i in range(len(digits)):
    		sum += digits[i] * pow(10, len(digits) - 1 -i)
    		sum_str = str(sum + 1)
    		return [int(j) for j in sum_str]