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

class PositionalList(_DoubleLinkedBase):
	class Node:
		'__slots__'='_element','_next','_prev'
		def __init__(self,element,next,prev):
			self._element=element
			self._next=next
			self._prev=prev

	class Position:
		def __init__(self,container,node):
			self._container=container
			self._node=node

		def element(self):
			return self._node._element

		def __eq__(self,other):
			return type(self) is type(other) and self._node=other._node

		def __ne__(self,other):
			return not(self==other)
#___________________________________________UTILITY METHODS________________________________
	def _validate(self,p):
		if not isinstance(p, self.Position):
			raise TypeError('p must be proper Position type')

		if p._container is not self:
			raise ValueError('p doesnt belong to this container')

		if p._node._next is None:
			raise ValueError('p is no longer valid Position')

		return p._node

	def _make_position(self,node):
		if node is self._header or node is self._trailer:
			return None
		return self.Position(self,node)
#____________________________________________ACCESSORS______________________________________
	def first(self):
		return self._make_position(self._header._next)

	def last(self):
		return self._make_position(self._trailer._prev)

	def before(self,p):
		node=self._validate(p)
		return self._make_position(node._prev)

	def after(self,p):
		node=self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		cursor=self.first()
		while cursor is not None:
			yield cursor.element()
			cursor=self.after(cursor)
#___________________________________________MUTATORS_________________________________________
	def _insert_between(self,e,predecessor,successor):
		node=super()._insert_between(e,predecessor,successor)
		return self._make_position(node)

	def add_first(self,e):
		return self._insert_between(e,self._header,self._header._next)
	
	def add_last(self,e):
		return self._insert_between(e,self._trailer._prev,self._trailer)

	def add_before(self,p,e):
		original=self._validate(p)
		return 	self._insert_between(e,original._prev,original)

	def delete(self,p):
		original=self._validate(p)
		self/_delete_node(original)

	def replace(self,p,e):
		original=self._validate(p)
		old_value=original._element
		original._element=e
		return old_value

	def _insertion_sort(self):
		if len(self)>1:
			marker=self.first()
			while marker!=self.last:
				pivot= self.after(marker)
				value=	pivot.element()
				if value>marker.element():
					marker=pivot
				else:
					walk=marker
					while walk!=self.first() and self.before(walk).element()>value:
						walk=self.before(walk)
					self.delete(pivot)
					self.add_before(walk,value)

	def sort(self):
		self._insertion_sort()
		return self
	

	