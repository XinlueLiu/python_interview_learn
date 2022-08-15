# given an integer array nums, return true if any value appears at least twice. return falste if 
# every element is distinct

def contains_duplicates(nums):
    # maintain a dictionary, key being each item in the list
    # if encoutner another same key, return True
    # if exausted entire list and still not find another key, return False
    res_dict = {}
    for n in nums:
        if (n in res_dict):
            return True
        else:
            res_dict[n] = 1
    return False

nums = [1,1,1,3,3,4,3,2,4,2]
sol = contains_duplicates(nums)
print(sol)