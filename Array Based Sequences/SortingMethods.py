def find_min(array):
	smallest=array[0]
	j=0
	for i in range(len(array)):
		if array[i]<smallest:
			smallest=array[i]
			j=i
	return j

def SelectionSort(array):
	'''Algorithm --- >>> Find smallest element in array[i:] and swap with array[0] of array[i:], i>=0'''
	l=len(array)
	for i in range(l):
		print(array[i], array[i+find_min(array[i:])])
		temp=array[i]
		array[i]=array[i+find_min(array[i:])]
		array[i+find_min(array[i:])]= temp
	return array

def SelectionSort(array,n):
	for i in range(n-1):
		imin=i
		for j in range(i,n):
			if array[j]<array[imin]:
				imin=j
		array[i],array[imin]=array[imin],array[i]
	return array

a=[8,4,7,2,10,3]

print(SelectionSort(a,6))