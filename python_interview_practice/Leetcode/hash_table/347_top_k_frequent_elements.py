
def find_k_frequent_numbers(nums,k):
    # create a count table with size len(nums) to document numebr of occurance for each element. 
    # The key is number of occurances, and we will have at most len(nums) numbers of duplicate variables
    # range(n) will create n iterables, but we want n+1
    count_list = [[] for i in range(len(nums) + 1)]
    dict_count = {}
    # count number of occurances and push to dictioanry
    # key is list item, value is number of occurance
    for n in nums:
        if (n in dict_count):
            dict_count[n] += 1
        else:
            dict_count[n] = 1
    # append key(with is the list item) to count list location[value], which is number of occurance
    # print(dict_count)
    for val,cnt in dict_count.items():
        count_list[cnt].append(val)
    # result element. We want top k elements
    # print(count_list)
    res = []
    # loop through the count_list in descending order
    # len(count_list) - 1 because len(count_list) will return n, but count_list[n] does not exist
    # from last item to 0, with step 1
    for i in range(len(count_list) - 1, 0, -1):
        # each count_list[i] may have multiple items
        for n in count_list[i]:
            res.append(n)
            # if has up to k elements, return
            if len(res) == k:
                return res

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    sol = find_k_frequent_numbers(nums,k)
    print(sol)