import math
class Progression:
	def __init__(self,start=0):
		self._current=start
	def _advance(self):
		self._current+=1
	def __next__(self):
		if self._current is None:
			raise StopIteration()
		t=self._current
		self._current +=1
		return t
	def __iter__(self):
		'''an iterator must return itself as an iterator'''
		return self
	def print_progression(self,n):
		'''print next n values'''
		print(' '.join(str(next(self))) for j in range(n))
class ArithematicProgression(Progression):
	def __init_(self,increment=1,start=1):
		super().__init_(start)
		self._increment=increment
	def _advance(self):
		self._current += self._increment
class GeometricProgression(Progression):
	def __init__(self, base=2,start=1):
		super().__init__(start)
		self._base=base
	def _advance(self):
		self._current *=self._base
class FibonacciProgression(Progression):
	"""docstring for FibonacciProgression"""
	def __init__(self,first=0,second=1):
		super().__init__(first)
		self._prev = second-first
	def _advance(self):
		self._prev,self._current=self._current,self._prev+self._current
class VariationFibonacciProgression(Progression):
	def __init__ (self,first=2,second=200):
		super().__init__(first)
		self._prev= first- second if first- second > 0 else second -first
	def _advance(self):
		self._prev,self._current=self._current,abs(self._current- self._prev)
class SquareRootProgression(Progression):
	def __init__(self,first=math.sqrt(65536.0)):
		super().__init__(self,first)
		self._prev=float(first)*float(first)
	def _advance(self):
		self._prev, self._current = self._current , math.sqrt(float(self._current))

def findno(first,second,k):
	result=FibonacciProgression(first,second)
	for i in range(8):
		result.__next__()
	return result._current
a=VariationFibonacciProgression()
print(a.print_progression(9))




