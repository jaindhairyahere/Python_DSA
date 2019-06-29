import ctypes			# To get a raw low level array

class MyDynamicArray:
	''' A Dynamic Array similar to Python's List'''
	def __init__(self):
		'''Create an empty array'''
		self._n=0
		self._capacity=1
		self._A=self._make_array(self._capacity)		# initializing a low level array

	def __len__(self):
		'''Returns Number of elements stored in array'''
		return self._n

	def capacity(self):
		return self._capacity

	def __getitem__(self,k):
		'''Returns element at index k form the array'''
		if not 0<=k<=len(self):
			raise IndexError('Invalid Index')
		return self._A[k]

	def append(self,obj):
		'''Add object to end of the array'''
		if self._n==self._capacity:
			self._resize(2*self._capacity)
		self._A[self._n]=obj
		self._n +=1

	def _resize(self,c):
		'''Resize internal array to size : c'''
		B=self._make_array(c)
		for k in range(self._n):
			B[k]=self._A[k]
		self._A=B
		self._capacity=c

	def _make_array(self,c):
		'''Returns a new array with capacity : c'''
		return(c*ctypes.py_object)()

	def print(self):
		print('{{{')
		for i in range(self._n):
			print(self._A[i] ,)
		print('}}}')

import sys
data=MyDynamicArray()
#a=len(data)
#b=data.capacity()
#print('Length: {0:3d}; capacity: {1:4d}'.format(a, b))	
#for k in range(30):
#	data.append(None)
#	a=len(data)
#	b=data.capacity()
#	print('Length: {0:3d}; capacity: {1:4d}'.format(a, b))

import time
def compute_average(n):
	'''Performs n appends to an empty list'''
	data=[]
	start=time.time()
	for k in range(n):
		data.append(None)
	end=time.time()
	return (end-start)/n
print(compute_average(100000))

