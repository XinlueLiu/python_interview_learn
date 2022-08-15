# Given an unsorted array nums, return length of longest consecutive element sequences
# in order to find longest consecutive sequence, i need to find consecutive sequences, and return the longest
# find the start of sequence by checking if there num-1 exists in the list
# maintain a dictioanry key being the start of sequence, and value is the longest consecutive length

def find_lcs(nums):
    res_dict = {}
    for n in nums:
        if (n - 1 not in nums):
            # create a new sequence
            res_dict[n] = 0
            # keep finding the consecutive numbers
            length = 0
            while(n + length in nums):
                res_dict[n] += 1
                # increment the length
                length += 1
    # can maintain the list of values and sort in reverse order to get the largest value, but not the most efficient
    con_list = list(res_dict.values())
    con_list.sort(reverse=True)
    return con_list[0]

def find_lcs_efficient(nums):
    # no need to maintain a dictionary because we only need to find length
    # maintain a maxlength variable to count the maximum consecutive length 
    maxLength = 0
    for n in nums:
        if (n - 1 not in nums):
            # maintain a local length
            length = 0
            while(n + length in nums):
                length += 1
            # update maxlength if find a new longer consecutive sequence
            maxLength = max(length, maxLength)
    return maxLength


nums = [100,4,200,1,3,2]
sol = find_lcs_efficient(nums)
print(sol)

# TODO: maintain a local length and a global maxlength. Update maxlength while comparing
# no need to maintain a dictionary because no need to know the start of sequence.
# dict.values and dict.keys will return a tuple. need to convert to a list to perform sort. can sort reverse