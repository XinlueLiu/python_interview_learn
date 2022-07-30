from typing import List

# This is the brute force way
# class Solution:
#     def __init__ (self, nums = [], target = 0):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         nums = self.nums
#         target = self.target
#         for itr in range(len(nums)):
#             for nxt_itr in range(itr+1, len(nums)):
#                 if (nums[itr] + nums[nxt_itr] == target):
#                     return [itr, nxt_itr]
#         return []

class Solution:
    def __init__ (self, num, target):
        self.num = num
        self.target = target
    
    def twoSum(self):
        num = self.num
        target = self.target
        # create a dictionary that holds the key = content, value = index
        res_dict = {}
        # enumerate returns two loop variables
        # count of current iteration, and value of the item at the current iteration
        for key,value in enumerate(num):
            # see if the key(content in this case) exist in the newly created dictionary
            if (target - value) in res_dict:
                return [res_dict[target - value], key]
            res_dict[value] = key
        return []

if (__name__ == '__main__'):
    sol_list = []
    sol_2Sum = Solution([2,7,11,15],9)
    sol_list = sol_2Sum.twoSum()
    print(sol_list)
    #range(1,6) = 1,2,3,4,5
    