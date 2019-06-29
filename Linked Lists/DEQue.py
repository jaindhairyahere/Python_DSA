class Empty(Exception):
	pass

class Node:
	'__slots__'='_element','_next','_prev'
	def __init__(self,element,next,prev):
		self._element=element
		self._next=next
		self._prev=prev

class _DoubleLinkedBase:
	def __init__(self):
		self._header=Node(None,None,None)
		self._trailer=Node(None,None,None)
		self._header._next=self._trailer
		self._trailer._prev=self._header
		self._size=0

	def __len__(self):
		return self._size

	def is_empty(self):
		return len(self)==0

	def _insert_between(self,e,pre,post):
		new=Node(e,pre,post)
		pre._next=new
		post._prev=new
		self._size+=1
		return new

	def _delete_node(self,node):
		pre=node._prev
		post=node._next
		pre._next=post
		post._prev=pre
		self._size-=1
		element=node._element
		node._prev=node._next=node._element=None
		return element

class LinkedDeque(_DoubleLinkedBase):
	def first(self):
		if self.is_empty():
			raise Empty('Deque is Empty')
		return self._header._next._element

	def last(self):
		if self.is_empty():
			raise Empty('Deque is Empty')
		return self._trailer._prev._element

	def insert_first(self,e):
		self._insert_between(e,self._header,self._header._next)

	def insert_last(self,e):
		self._insert_between(e,self._trailer._prev,self._trailer)

	def delete_first(self):
		if self.is_empty():
			raise Empty('Deque is Empty')
		self._delete_node(self._header._next)

	def delete_last(self):
		if self.is_empty():
			raise Empty('Deque is Empty')
		self._delete_node(self._trailer._prev)





	