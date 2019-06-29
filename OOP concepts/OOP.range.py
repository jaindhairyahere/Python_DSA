import time
start_time= time.time()
# Overriding Range function
from abc import ABCMeta, abstractmethod
import collections

class Sequence(metaclass = ABCMeta):
	@abstractmethod
	def __len__(self):

	@abstractmethod
	def __getitem__(self):
	
	def __contains__(self,val):
		for j in range(len(self)):
			if self[j]==val:
				return True
		return False
	def index(self,val):
		for j in range(len(self)):
			if self[j]==val:
				return j
		raise ValueError
	def count(self,val):
		k=0
		for j in range(len(self)):
			if self[j]==val:
				k+=1
		return k
		
class Range(collections.Sequence):
	def __init__(self, start = None, stop = None, step=1):
		if step==0:
			raise ValueError("Step Value can't be Zero")
		if stop==None:				# case when Range(n) is used
			start,stop=0,start
		self._length = ((stop-start-1)//step)+1
		self._start=start
		self._step=step
	def __len__(self):
		return self._length
	def __getitem__(self,k):
		if k<0:
			k +=len(self)
		if not 0<=k<self._length:
			raise IndexError("Index Out Of Range")
		return self._start+k*self._step
	def __contains__(self,k):
		stop=self._start +self._length*self._step
		if stop==None:				# case when Range(n) is used
			self._start,stop=0,self._start
		if k in range(self._start,stop):
			return True
		else:
			return False

r= Range(0,10,2)

if 999999 in range(10000000):
	print (True)
end_time=time.time()
print(end_time-start_time)


if 2 in Range(10000000):
	print (True)

print(r[3])
print()
print()
end_time=time.time()
print(end_time-start_time)
