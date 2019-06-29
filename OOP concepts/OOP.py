class CreditCard:
	def __init__(self,customer,bank,acnt,limit):
		self._customer= customer
		self._bank = bank
		self._acnt=acnt
		self._limit=limit
		self._balance=0
	def get_customer(self):
		return self._customer
	def get_bank(self):
		return self._bank
	def get_acnt(self):
		return self._acnt
	def get_limit(self):
		return self._limit
	def get_balance(self):
		return self._balance
	def charge(self,price):
		if price + self._balance>self._limit:
			return False
		else:
			self._balance +=price
			return True
	def make_payment(self,amount):
		self._balance -=amount
		return True
if __name__=='__main__':
	wallet=[]
	wallet.append(CreditCard("Dhairya","SBI",'180080006',800))
	wallet.append(CreditCard("Dhairya","Canara",'180080011',900))
	wallet.append(CreditCard("Dhairya","SBI Current",'180080006',1000))

for val in range(1,17):
	wallet[0].charge(val)
	wallet[1].charge(2*val)
	wallet[2].charge(3*val)

for c in range(3):
	print('Customer =', wallet[c].get_customer())
	print('Bank =', wallet[c].get_bank())
	print('Account =', wallet[c].get_acnt())
	print('Limit =', wallet[c].get_limit())
	print('Balance =', wallet[c].get_balance())
	while wallet[c].get_balance()>100:
		wallet[c].make_payment(100)
		print('New Balance =',wallet[c].get_balance())
	print()
print()
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# self and other are used to refer to 2 instances of the same class
class Vector:
	def __init__(self,d):
		self._coords=[0]*d 			# array of length d with initial values gets created

	def __len__(self):
		return len(self._coords)
	def __getitem__(self,j):
		return self._coords[j]
	def __setitem__(self,j,val):
		self._coords[j]=val
	def  __add__(self, other):						#Operator Overloading ---> + operator overloaded
		if len(self)!=len(other):
			raise ValueError('Dimentions must Agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j]=self[j]+other[j]
		return result
	def __eq__(self,other):							#Operator Overloading ---> = operator overloaded
		return self._coords==other._coords

	def __ne__(self,other):
		return not self==other			# Rely on existing(newly overloaded) == definition
	def __str__(self):
		return '<' + str(self._coords)[1:-1]+ '>'	
v = Vector(5) # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23 # <0, 23, 0, 0, 0> (based on use of setitem )
v[-1] = 45 # <0, 23, 0, 0, 45> (also via setitem )
print(v[4]) # print 45 (via getitem )
u=v+v # <0, 46, 0, 0, 90> (via add )
print(u) # print <0, 46, 0, 0, 90>
total = 0
for entry in v: # implicit iteration via len and getitem
	total += entry
print()
print()
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Overriding Range function
class Range:
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

r= Range(0,10,2)
print(r[3])
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Shallow And Deep Copy
''' lets have a nested list '''
A=[[1,2,3],[4,5,6],[7,8,9]]
print(id(A))
B=A
print(id(B), "Copying Not Performed")

C=list(A)
print(id(C), "Copying done")

''' So C is a Copy of A. How good is the copy........'''
C.append([10,11,12])
print("C = ",C," A = ", A)
print(id(C[1]) , id(A[1]))
C[1]=[100,200,300]
print(A[1])
print (id(C[1]),id(A[1]))

C[1]=[4,5,6]
print (id(C[1]),id(A[1]))					# non nested elements are separate for C and A

print(id(C[1][0]),id(A[1][0])) 				# nested elements have same id (Shallow Copy)

import copy
D=copy.deepcopy(A)
D[0][0]=100
print(id(D[0][0]),id(A[0][0]))				#nested elements have different id (Deep copy)
'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
