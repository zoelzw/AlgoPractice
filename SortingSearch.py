# Recursive 
def BinarySearch(nums,left,right,target):
    while right >= left:
        mid = (right+left) // 2 
        if nums[mid] > target:
            return BinarySearch(nums,left,mid-1,target)
        elif nums[mid] < target:
            return BinarySearch(nums,mid+1,right,target)
        else:
            return mid 
    return -1 


# Iterative Binary Search Function
def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1
		else:
			return mid
	return -1


# Test array
arr = [-100,-8,1,2,3,5,44]
x = 3

# Function call
result = binary_search(arr, x)
result1 =BinarySearch(arr,0,len(arr)-1,x)
print(result)
print("BinarySearch", result1)