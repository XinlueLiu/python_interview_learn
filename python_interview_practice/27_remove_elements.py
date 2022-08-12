
class Sol_remove_elements:
    def __init__ (self, nums, target):
        self.nums = nums
        self.target = target

    def remove_element_extra_memory(self):
        new_list = []
        for each_val in nums:
            if (each_val != target):
                new_list.append(each_val)
        print(f'numbers of remaining element is {len(new_list)}')
        return new_list

    def remove_element(self):
        # go through the loop, and maintain 2 pointers. right pointer go through the list
        # value get assigned to left pointer position if right pointer value is not target
        # then left pointer get incremented by 1
        l_p = 0
        for r_p in nums:
            if (r_p != target):
                nums[l_p] = r_p
                l_p = l_p + 1
        print(f'numbers of remaining element is {l_p}')
        return nums[:l_p]

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    target = 2
    sol = Sol_remove_elements(nums, target)
    res = sol.remove_element()
    print(res)