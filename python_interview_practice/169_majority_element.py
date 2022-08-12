
class Sol_majority_element:
    def __init__(self, nums):
        self.nums = nums

    def find_majority_element(self):
        dict_res = {}
        # for each value in the list, construct a dictionary out of it
        # the key of dictionary is value of list item, value is the number of occurances of its key
        # sort the dictionary by value in descending order
        # find the value's key, which is the item with most occurances
        for each_item in nums:
            if (each_item in dict_res):
                dict_res[each_item] = dict_res[each_item] + 1
            else:
                dict_res[each_item] = 1
        # new_list[0] will be the numbers of most occurances, the value that we need to find the key
        new_list = sorted(dict_res.values(), reverse=True)
        for key,value in dict_res.items():
            if (value == new_list[0]):
                return key
        # return new_list[0][0]

if __name__ == "__main__":
    nums = [2,2,1,1,1,1,1,2,2]
    sol = Sol_majority_element(nums)
    res = sol.find_majority_element()
    print(res)