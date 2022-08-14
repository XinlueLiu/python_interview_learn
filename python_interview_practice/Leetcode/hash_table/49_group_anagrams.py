# returns a default value for the dictionary defined
from collections import defaultdict

def group_anagrams(strs):
    # find occurances of each elements of each string, use that as a dictionary key
    # the dictionary value will be strings with same key(same character count)
    # default to a list so it can use the append method later
    res_dict = defaultdict(list)
    for each_str in strs:
        count = [0] * 26 # 26 characters
        for each_c in each_str:
            # map a to 0, b to 1...
            # ord is the unicode. starts with a, a-a = 0 -> count[0] = a, then the actual value will be 
            # numebr of occurances 
            count[ord(each_c) - ord("a")] += 1
        # count is list but list cannot be dictionary key(because lists are mutable, and dictioanry keys are unique)
        # need to covert to a tuple, then append values(strs) with same characters occurances
        # use defaultdict because thie count may not exist in the dictionary, so python will create keyerror
        res_dict[tuple(count)].append(each_str)
    # dont care about keys, aka the counts
    return res_dict.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    res = group_anagrams(strs)
    print(res)