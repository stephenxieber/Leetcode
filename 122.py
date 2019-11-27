class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	res = 0
    	for i in range(1, len(prices)):
    		diff = prices[i] - prices[i - 1]
    		res += diff if diff >0 else 0
    	return res