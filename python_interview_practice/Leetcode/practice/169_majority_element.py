# given an array nums in size n, return the majority element
# create a dictionary, key being value, value being number of occurances

def find_majority_element(nums):
    res_dict = {}
    for n in nums:
        if n in res_dict:
            res_dict[n] += 1
        else:
            res_dict[n] = 1
    # now dictionary is 2:4, 1:3
    maxOccur = 0
    res = 0
    # loop through the dictionary. compare maxoccur with occurance of each key
    # if the key has more occurance, assign res to the key and update maxoccurance
    # or we can sort dictionary in values using res = sorted(dict_res.values, reverse = True) in descending order
    # then find res[0]'s key from the dictionary
    for key,val in res_dict.items():
        if maxOccur < val:
            maxOccur = val
            res = key
    return res

nums = [2,2,1,1,1,2,2]
sol = find_majority_element(nums)
print(sol)

# TODO: when updating the localmax remember to also have a res variable that update the key. we need to find the key, not the occurance