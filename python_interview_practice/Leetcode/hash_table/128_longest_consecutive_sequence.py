
def find_longest_consecutive_sequence(nums):
    # to avoid duplicates and improve efficiency
    numSet = set(nums)
    maxLength = 0
    for n in numSet:
        # check if the element is the starting sequence
        if (n - 1) not in numSet:
            # if the starting sequence, find the consecutive sequences
            length = 0
            while(n + length) in numSet:
                length += 1
            # while the consecutive sequences break, assign the maxlength
            maxLength = max(maxLength, length)
    return maxLength



if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    sol = find_longest_consecutive_sequence(nums)
    print(sol)