# given an array of strings, group the anagrams together

from collections import defaultdict

def group_anagram(strs):
    # dictionary that key -> matches numbers of occurances of each characters
    # e.g. for 1st group, key should be 1e1a1t
    # and for each string that matches this key, we append the str as value

    # for the key, we can create an list of 26 elements(each index represents one alphabet,
    # and the value of that index will be the number of occurances of that alphabet)
    # so for 1st group, [1,0,0,0,1,.......,1,..]
    # ord(e) - ord(a)

    # create a list of 26 elements
    # res_dict = {}
    res_dict = defaultdict(list)
    # look through each element, and assign them to the dictionary
    for each_str in strs:
        alpha_lu_table = [0] * 26
        # update the key for each str
        for each_c in each_str:
            alpha_lu_table[ord(each_c) - ord("a")] += 1
        # append this string to dictionary
        # list cannot be a dictioanry key since its mutable, we need to convert it to a tuple
        # key might not exist. need to check
        # need to check if the key has existed. If not, need to create a LIST and then append. Cannot append to Null
        # cannot initialize list(each_str) directly because its gonna divide each element
        res_dict[tuple(alpha_lu_table)].append(each_str)
        # if (tuple(alpha_lu_table) not in res_dict):
        #     res_dict[tuple(alpha_lu_table)] = []
        #     res_dict[tuple(alpha_lu_table)].append(each_str)
        # else:
        #     res_dict[tuple(alpha_lu_table)].append(each_str)
    return res_dict.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = group_anagram(strs)
    print(sol)

# TODO: 
# 1. initialize alpha_lu_table for each string round
# 2. list cannot be dictionary key, need to convert to tuples
# 3. if key does not exist, need to check that and initialize a list and then append. Or use defaultdict from collections, and initialize with a list