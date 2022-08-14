
def find_product_division(nums):
    # find res as the multiplication of all items
    # then just divide each element at its index
    # need work if contain 0 in nums
    res = 1
    for n in nums:
        res = res * n
    res_list = []
    for i in range(len(nums)):
        res_list.append(res/nums[i])
    return res_list

def find_product(nums):
    # for value n in [...,n,...], product of the array element except itself means that we are finding 
    # product of the prefix(product value before n) and postfix(product value after n)
    # we can go through nums left to right, find and place prefix in result list
    # then go through nums right to right, multiply the prefix in result list with postfix we just found
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        # update the prefix
        # [1,1,2,6]
        prefix = prefix * nums[i]
    postfix = 1
    # len(nums) is 4, we want to start from index [3]. range start will include start, but EXCLUDE end
    for i in range(len(nums) - 1, -1, -1):
        # nums    = [1,2,3,4]
        # res     = [1,1,2,6]
        # postfix = [24,12,4,1]
        #           [24,12,8,4]
        res[i] = postfix * res[i]
        postfix = postfix * nums[i]
    return res

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = find_product(nums)
    print(sol)