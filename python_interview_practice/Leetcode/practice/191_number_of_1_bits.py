# a function that takes an unsigned integer and return the numbers of 1 bits it has
# x - 1 will eliminate the last 1 in the binary
# by using x & (x-1), we will eliminate one "1" from the original binary
# keep doing until x & (x-1) = 0, then we know we have shifted all 1's from original string

# 101
# 100 -> 100
# 011 -> 0

def find_num_1(x):
    n = 0
    while x:
        x = x & (x-1)
        n += 1
    return n

n = 11
sol = find_num_1(n)
print(sol)

# or we can sum each variable of the list and the sum will be number of 1's
# [:2] because bin(n) will return string with leading 0b
# new_list = list(bin(n))[2:]
# print(new_list)
# num = 0
# for each_val in new_list:
#     num += int(each_val)
# print(num)