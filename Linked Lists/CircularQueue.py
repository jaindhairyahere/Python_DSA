class _Node:
	'__slots__'='_element','_next'
	def __init__(self,element,next):
		self._element=element
		self._next=next

class Empty(Exception):
	pass

class LinkedCircularQueue:
	def __init__(self):
		self._tail=None				#referring to current
		self._size=0

	def __len__(self):
		return self._size

	def is_empty(self):
		return len(self)==0

	def first(self):
		if self.is_empty:
			raise Empty('Queue is Empty')
		return self._tail._next._element

	def enqueue(self,e):
		self._size +=1
		tail_node=_Node(e,self._tail._next)
		if self.is_empty:
			self._tail=tail_node
		else:
			self._tail._next=tail_node
		self._tail=tail_node

	def dequeue(self):
		if self.is_empty:
			return Empty("Queue is Empty")
		old_head= self._tail._next
		if self._size==1:
			self._tail=None
		else:
			self._tail._next=old_head._next
		self._size-=1
		return old_head._element

	def rotate(self):
		if len(self)>0:
			self._tail=self._tail._next



























































































































