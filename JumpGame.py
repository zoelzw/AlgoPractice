def canJump(nums):
    lastIndex = len(nums) -1 
    right = 0 
    # reach = 0 
    if not nums:
        return False
    for index in range(len(nums)-1):
        if index <= right:
            right = max(right,index+nums[index])
    if right >= lastIndex:
        return True 
    else:
        return False


# nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
# nums = [0,2,3]
print(canJump(nums))