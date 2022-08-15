# given an integer array nums, return an array answer such that answer[i] is equal to product of all elements 
# of nums except nums[i]

# for a value n [...,n,...] in nums, we want to multiple everything before n and everything after n
# maintain a result list size of nums
# from left to right, assign the prefix to the index position
# prefix = 1 at the beginning, then multiplied with itself at its position to be the prefix of next value
#      [1,-1,-1,0,0] prefix = 1, -1, -1, 0, 
# go from right to left, multiple the each element in result by its postfix
# [1,-1,-1,0,0] 
# prefix = 1, -1, -1, 0, 0
# postfix = 0 ,0, -9, 3, 1 
# [1,0,9,0,0] 

def product_of_array_except_self(nums):
    # maintain a result list of size len(nums)
    res = [1] * len(nums)
    prefix = 1
    postfix = 1
    # from left to right, assigning prefix to res
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    # go from right to left, multiple postfix to prefix
    # reverse order, 1 step at a time
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

nums = [-1,1,0,-3,3]
sol = product_of_array_except_self(nums)
print(sol)

# TODO: remember range will INCLUDE starting index but EXCLUDE ending index