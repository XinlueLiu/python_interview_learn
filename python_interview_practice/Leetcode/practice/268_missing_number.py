# given an array nums containing n distinct numbers in the range [0,n], return the only number in the range that is missing
# one way is to sum (n+1) variables and subtract n variables. The result is the missing variable

def find_missing_number_sum(x):
    # find sum of arithmetic sequence
    n_sum = (len(x) * (len(x) + 1)) / 2
    x_sum = sum(x)
    res = n_sum - x_sum
    return int(res)

# the other way is to use xor
def find_missing_number_xor(nums):
    # xor every value in n
    # TODO: if do this dont forget to do range(len(nums) + 1!!!!!) range will discard the last variable
    res = 0
    for i in range(len(nums) + 1):
        res = res ^ i
    for i in nums:
        res = res ^ i
    return res

nums = [9,6,4,2,3,5,7,0,1]
sol = find_missing_number_xor(nums)
print(sol)