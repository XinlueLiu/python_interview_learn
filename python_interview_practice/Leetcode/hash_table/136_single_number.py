

class Sol_single_number:
    def __init__(self, a1):
        self.a1 = a1

    def find_sn_dict(self):
        a1 = self.a1
        # create a dictionary. key being each item in a1 list, value being number of occurance
        res_dict = {}
        for count, val in enumerate(a1):
            # if current item of list is a key of dictionary
            if (val in res_dict):
                # increment its value pair indicates that it has occured more than once
                res_dict[val] += 1
            else:
                # else initialize the content to be 1
                res_dict[val] = 1
            
        # loop through the dictionary and finds the one content that only occurs one time
        for key in res_dict.keys():
            if (res_dict[key] == 1):
                return key

    def find_sn_list(self):
        a1 = self.a1
        res_list = []
        # foreach value in list, if exist remove by its value. else append to the list
        # pop removes by index
        # del can remove items by index or slice
        for val in a1:
            if (val in res_list):
                res_list.remove(val)
            else:
                res_list.append(val)
        return res_list[0]

    def find_sn_bin(self):
        # use the property of xor
        # since we know we have 1 item that appears once and ALL other items appear two times,
        # we can use xor since xor two same numbers will be 0
        # then the remaining item xor 0 will be itself
        res = 0
        for val in self.a1:
            res = val ^ res
        return res


if __name__ == '__main__':
    a1 = [1,0,1]
    sol = Sol_single_number(a1)
    res = sol.find_sn_bin()
    print(res)