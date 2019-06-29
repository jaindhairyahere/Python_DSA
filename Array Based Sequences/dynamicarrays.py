import sys
data=[]
a=len(data)
b=sys.getsizeof(data)
print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))	
for k in range(30):
	data.append(None)
	a=len(data)
	b=sys.getsizeof(data)
	print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
	data.pop()
	data.append(k)
	a=len(data)
	b=sys.getsizeof(data)
	print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))			# Whatever I append, getsizeof(data) returns the same value
#	data.pop()
#	data.append(None)
print(data)

string= "Since List is A referencial structure, Presence of element wont change its size. It just stores the reference of that element whoose size is constant(= 8bytes on 64 bit system)"
print(string)
data=[]
data.append(None)
print(sys.getsizeof(data))