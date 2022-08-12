

class Sol_merge_sorted_array:
    def __init__ (self, a1, len_a1, a2, len_a2):
        self.a1 = a1
        self.a2 = a2
        self.len_a1 = len_a1
        self.len_a2 = a2
    
    def merge(self):
        # delete additional a1 element
        del a1[len_a1:]
        # extend adds entire list to the end of a1 list
        a1.extend(a2)
        a1.sort()
        return a1



if __name__ == "__main__":
    a1 = [1,2,3,0,0,0]
    a2 = [2,5,6]
    len_a1 = 3
    len_a2 = len(a2)
    sol = Sol_merge_sorted_array(a1, len_a1, a2, len_a2)
    merged_array = sol.merge()
    print(merged_array)