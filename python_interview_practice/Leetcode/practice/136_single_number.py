# use the property of xor. xor two same numbers will be itself

def find_single_num_xor(nums):
    res = 0
    for n in nums:
        res = res ^ n
    return res

# or use a dictionary. first occurance will be pushed to dictionary
# second occurance, dictionary will pop the key-value pair. So there will be one item left in the dictionary
# return its key, which is the single value
def find_single_num_hash(nums):
    res_dict = {}
    for n in nums:
        if (n in res_dict):
            res_dict.pop(n)
        else:
            res_dict[n] = 1
    res = list(res_dict.keys())
    return res[0]

nums = [4,1,2,1,2]
sol = find_single_num_hash(nums)
print(sol)