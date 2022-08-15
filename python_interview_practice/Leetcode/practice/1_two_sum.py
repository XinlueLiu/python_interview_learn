# arrays of nums, target
# indices of two nums that add up to target

def find_two_sum(nums, target):
    # go through the list left to right
    # for each item in the list, we look up in the dictioanry that if (target - item) exists in the dictionary
    # if not, add the item to the dictionary. dict[val] = index of the current item!!!!!!!!
    # 1:0, 2:1, 3:2, 
    res_dict = {}
    for index, val in enumerate(nums):
        if ((target - val) in res_dict):
            return [index, res_dict[target - val]]
        else:
            res_dict[val] = index
    return []

if __name__ == "__main__":
    nums = [1,2,3,4]
    # need to return [2,3] as indices
    target = 7
    sol = find_two_sum(nums,target)
    print(sol)

    # TODO:
    # 1. push dict[val] = index, not dict[target-val] = index
    # 2. loop through the list, not dictionary