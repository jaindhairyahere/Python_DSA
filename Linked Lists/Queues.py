class _Node:
	'__slots__'='_element','_next'
	def __init__(self,element,next):
		self._element=element
		self._next=next

class Empty(Exception):
	pass

class LinkedQueue:
	def __init__(self):
		self._head=None
		self._tail=None
		self._size=0

	def __len__(self):
		return self._size

	def is_empty(self):
		return len(self)==0

	def first(self):
		if self.is_empty:
			raise Empty('Queue is Empty')
		return self._head._element

	def enqueue(self,e):
		self._size +=1
		tail_node=_Node(e,None)
		if self.is_empty:
			self._head=tail_node
		else:
			self._tail._next=tail_node
		self._tail=tail_node
	def dequeue(self):
		if self.is_empty:
			return Empty("Queue is Empty")
		answer= self._head._element
		self._head=self._head._next
		self._size-=1