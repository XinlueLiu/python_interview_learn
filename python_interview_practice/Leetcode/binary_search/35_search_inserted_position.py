
class Sol_search_inserted_position_dictionary:
    def __init__ (self, list1, target):
        self.list1 = list1
        self.target = target

    def search_inserted_position(self):
        # create a new dictionary
        new_dict = {}
        # for each item in the list, construct the key-value pair of new dictionary
        # key being the index, and value being the list value
        for count,value in enumerate(self.list1):
            new_dict[count] = value

        # for each item in the dictionary, check if the item value is target value
        # if it is or the value has exceeds target value, return current index(since the list is already sorted)
        for key,value in new_dict.items():
            if (value >= self.target):
                return key
        # if still cannot find the target or values greater than target after exhausting the entier list
        # we know that the target is greater than the largest number of the list
        # return the length of the list as if target exists, it would be the last index + 1
        return len(self.list1)

class Sol_search_inserted_position_binary_search:
    def __init__ (self, list1, target):
        self.list1 = list1
        self.target = target

    def search_inserted_position (self):
        nums = self.list1
        target = self.target
        
        l,r = 0, len(nums) - 1
        while l <= r:
            # floor division. like integer division
            mid = (l+r) // 2
            if (target == nums[mid]):
                return mid
            
            if (target > nums[mid]):
                l = mid + 1
            if (target < nums[mid]):
                r = mid - 1

        # if never find the target
        return l
                


if __name__ == '__main__':
    list1 = [1,3,5,6]
    target = 7
    # sol_search = Sol_search_inserted_position_dictionary(list1,target)
    sol_search = Sol_search_inserted_position_binary_search(list1,target)
    result = sol_search.search_inserted_position()
    print(f'inserted_position is {result}')