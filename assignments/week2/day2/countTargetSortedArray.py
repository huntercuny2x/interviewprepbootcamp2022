#Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
#Output: 3

def count(arr, target):
	#search for leftmost idx
	left = binarySearch(arr, target, True)
	#target not in array
	if left < 0: return 0
	#search for rightmost idx
	right = binarySearch(arr, target, False)

	return right - left + 1


def binarySearch(arr, target, leftmost):
	low = 0
	high = len(arr) - 1

	idx = -1

	while(low <= high):
		mid = (low+high)//2
		#check right half of array if target 
		#is greater than middle value
		if target > arr[mid]:
			low = mid + 1
		elif target < arr[mid]:
			high = mid - 1
		else:
			idx = mid
			#if we are looking for leftmost idx
			if leftmost:
				high = mid - 1
			#if we are looking for rightmost idx
			else:
				low = mid +	1 

	return idx


arr = [1,2,2,3,3,4,5,6]
target = 2

x = count(arr, target)

print(x)


#Time complexity: O(logn)
#Space complexity: O(1)



