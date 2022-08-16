# Given an integer array nums and an integer k, return the k most frequent elements
# maintain a dictionary, that key being the item, value being the number of occurances
# TODO: 1. need to maintain a count table to count top k elements. we know we have at most len(nums) occurances
# 2. each number of occurance may have duplicate numbers, thats why for each entry of count table we are maintaining a list
# 3. size of 2D list need to be: range + 1 because 0 occurance makes no sense

def top_k_frequent_elements(nums,k):
    res_dict = {}
    # index is number of occurances
    # value are lists that are numbers that have the same # of occurances
    cnt_table = [[] for i in range(len(nums) + 1)]
    # assign the dictioanry
    for n in nums:
        if (n not in res_dict):
            res_dict[n] = 1
        else:
            res_dict[n] += 1
    # assign the count table
    for val,cnt in res_dict.items():
        cnt_table[cnt].append(val)
    # find the most k occurances
    # cnt table is handy because the index is already sorted(not exlicitly but by rules)
    # loop from end to 1(no need to check 0)
    print(cnt_table)
    res = []
    for i in range(len(nums), 0, -1):
        # append each value in the cnt_table inner list
        for n in cnt_table[i]:
            res.append(n)
            # only append up to k elements
            if (len(res) == k):
                return res


nums = [1,1,1,2,2,3,4,5,6,6,6,6,6,6,9]
k = 2
sol = top_k_frequent_elements(nums,k)
print(sol)