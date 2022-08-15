# given an integer n, return true if it is a power of two. Otherwise return false
# n is power of 2 if keep dividing its gonna return 1

def find_po2(n):
    while(n > 1):
        n = n / 2
    return n == 1

# 1,2,4,8,16,32,64
# 1,10,100,1000,10000,100000
# a trick that if n & (n - 1) == 0, then its power of 2(means it only has a leading 0)
def find_po2_binary(n):
    return n > 0 and n & (n - 1) == 0


n = 16
sol = find_po2_binary(n)
print(sol)