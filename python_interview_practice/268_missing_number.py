
def find_missing_number_xor(nums):
    res1 = 0
    # xor each number pf [0...n]
    for element in range(0,len(nums)+1):
        res1 = res1 ^ element
    for element in nums:
        res1 = res1 ^ element
    return res1

def find_missing_number_sum(nums):
    # arithmetic sequence
    res1 = (len(nums) * (len(nums) + 1)) / 2
    res2 = 0
    for val in nums:
        res2 = res2 + val
    return res1 - res2

if __name__ == "__main__":
    nums = [3,0,1]
    # two solutions
    # first method is to utilize the property of xor
    # xor each element of nums and each element of [0,n], the result will be the missing number
    # because the missing number in [0,n] will not appear in nums
    res1 = find_missing_number_xor(nums)
    print(res1)
    # should method is to subtract sum([0...n]) from sum(nums)
    # the difference will be the remaining number
    res2 = find_missing_number_sum(nums)
    print(res2)