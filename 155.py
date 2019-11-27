class MinStack:
	def __init__(self):

		self.data = []
		self.helper = []

	def push(self, x: int) -> None:
		self.data.append(x)
		if len(self.helper) == 0 or x <= self.helper[-1]:
			self.helper.append(x)

	def pop(self) -> None:
		top = self.data.pop()
		if self.helper and self.helper[-1] == top:
			self.helper.pop()
		return top

	def top(self) -> int:
		if self.data:
			return self.data[-1]

	def getMin(self) -> int:
		if self.helper:
			return self.helper[-1]