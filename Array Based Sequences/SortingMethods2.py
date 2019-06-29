def InsertionSort(A,n):
	'''	Algorithm InsertionSort(A):
	Input: An array A of n comparable elements
	Output: The array A with elements rearranged in nondecreasing order
	for k from 1 to n − 1 do
	Insert A[k] at its proper location within A[0], A[1], ..., A[k] '''
	for i in range(1,n):
		temp=A[i]
		hole=i
		for j in range(1,i):
			if A[j-1]<=A[i]<=A[j]:
				k=j
				break
		'''let A[k-1]<A[i]<A[k]'''
		
		for j in range(i,k,-1):
			A[i]=A[i-1]
		A[k]=temp
	return A

def InsertSort(A,n):
	for i in range(1,n):
		value=A[i]
		hole=i
		while hole>0 and A[hole-1]>value:
			A[hole]=A[hole-1]
		A[hole]=value
	return A
A=[7,2,4,1,5,3]
print(InsertSort(A,6))