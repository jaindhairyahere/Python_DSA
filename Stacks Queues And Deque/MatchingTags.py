class Empty(Exception):
	pass
class Stack:
	def __init__(self):
		self._A=[]
		self._n=0
	def push(self,e):
		(self._A).append(e)
		self._n+=1
	def pop(self):
		if self._n == 0:
			raise IndexError('Stack is Empty')
		(self._A).pop()
		self._n-=1
	def __len__(self):
		return self._n
	def __getitem__(self,k):
		return (self._A)[k]
	def is_empty(self):
		if len(self)==0:
			return True
		else:
			return False
	def top(self):
		if self.is_empty()==0:
			raise Empty('Empty Stack')
		return self._A[-1]
	def print(self):
		s= '{0}{1}{2}'.format("[",self._A,"]")
		return s

class GoodFile:
	def __init__(self):
		Opening=[]
		Closing=[]
	def readstring(self,string):
		for i in string:
			if i=='<':
				append(i)
					