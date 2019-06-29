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


def GoodExpression(string):
	S=Stack()
	i=0
	dic={'{':'}','[':']', '(':')'}
	while True and i<len(string):
		char= string[i]
		if not (char.isalpha()):
			S.push(char)
		if len(S)>1:
			if (S[-2] in dic) and S[-1]==dic[S[-2]]:
				S.pop()
				S.pop()
		i+=1
	if S.is_empty():
		return True
	return False
