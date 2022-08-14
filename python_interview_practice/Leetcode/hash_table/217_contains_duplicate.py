
def find_duplicate(nums):
    # create a hash map, loop through the nums list
    # everytime encounter a value, update the dictionary with key being the value
    # if encountered again, return True
    # if exausted the entire list and still haven't found duplicate, return false
    res_list = {}
    for n in nums:
        if (n in res_list.keys()):
            return True
        else:
            res_list[n] = 1
    return False


if __name__ == "__main__":
    nums = [1,2,3,1]
    # find the duplicate value in the list
    sol = find_duplicate(nums)
    print(sol)