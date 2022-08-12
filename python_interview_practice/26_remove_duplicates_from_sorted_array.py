

class Sol_remove_duplicates_from_sorted_array:
    def __init__(self, nums):
        self.nums = nums

    def remove_duplicates_set(self):
        # since set only contains unduplicated data, can convert the original list to a set
        # then convert back to a list to return
        new_set = set(self.nums)
        new_list = list(new_set)
        return new_list

    def remove_duplicates_extra_memory(self):
        # move along the list, append each list item to a new list if not already in the new list
        nums = self.nums
        new_list = []
        for each_val in nums:
            if (each_val not in new_list):
                new_list.append(each_val)
        print(f'number of distinct value is {len(new_list)}')
        return new_list

    def remove_duplicates(self):
        # maintain two pointers start at position 1, right pointer scan through the array
        # left pointer will point to the first duplicated item
        # Whenever right pointer finds a distinct value, its going to assign that value to where left pointer points
        # left pointer is updated + 1
        nums = self.nums
        l_p = 1
        for r_p in range(1, len(nums)):
            if (nums[r_p - 1] != nums[r_p]):
                nums[l_p] = nums[r_p]
                l_p = l_p + 1
        print(f'number of distinct value is {l_p}')
        return nums

if __name__ == "__main__":
    nums = [1,1,2,2,2,2,3,3,4]
    sol = Sol_remove_duplicates_from_sorted_array(nums)
    res = sol.remove_duplicates()
    print(res)