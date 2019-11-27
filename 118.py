class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
    	triangle = []
    	for row_num in range(numRows):
    		row = [None for _ in range(row_num + 1)]
    		row[0], row[-1] = 1, 1
    		for i in range(1, row_num):
    			row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
    		triangle.append(row)
    	return triangle