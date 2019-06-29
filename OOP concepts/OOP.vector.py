class Vector:
	def __init__(self,d):
		self._coords=[]
		if type(self._coords)==type(d):
			''' to pass Vector(sequence)'''
			self._coords=d
		elif type(d)==type(1):
			''' to pass Vector(length)'''
			self._coords = [0]*d
	def __len__(self):
		'''to use len(V)'''
		return len(self._coords)
	def __getitem__(self,j):
		'''to use V[i]'''
		return self._coords[j]
	def __setitem__(self,j,val):
		'''to assign using V[i]=j'''
		self._coords[j]=val
	def  __add__(self, other):						#Operator Overloading ---> + operator overloaded
		if len(self)!=len(other):
			raise ValueError('Dimentions must Agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j]=self[j]+other[j]
		return result
	def  __radd__(other, self):						# TO use b + a (for a)
		return self.__add__(other)
	def  __sub__(self, other):						#Operator Overloading ---> - operator overloaded
		if len(self)!=len(other):
			raise ValueError('Dimentions must Agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j]=self[j]-other[j]
		return result
	def  __mul__(self, other):						#Operator Overloading ---> * operator overloaded
		if type(self)==type(other):
			if len(self)!=len(other):
				raise ValueError('Dimentions must Agree')
			result = 0
			for j in range(len(self)):
				result +=self[j]*other[j]
			return result
		else:
			result = Vector(len(self))
			for j in range(len(self)):
				result[j] +=self[j]*other
			return result
	def __rmul__(k,self):						# To use k*V (for V)
		return self.__mul__(k)
	def __neg__(self):							#To use -(V)
		return self.__mul__(-1)
	def __eq__(self,other):							#Operator Overloading ---> == operator overloaded
		return self._coords==other._coords

	def __ne__(self,other):
		return not self==other			# Rely on existing(newly overloaded) == definition
	def __str__(self):
		return '<' + str(self._coords)[1:-1]+ '>'														