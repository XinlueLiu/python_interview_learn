# given an integer n, return true if it is a power of 4
# method 1 is to keep dividing until num is less than 1
# then if it is power of 4, the result must be 1

def po4(n):
    while(n > 1):
        n /= 4
    return n == 1

# 1,4,16,64,256
# 1, 100, 10000
# 1. it must be power of 2
# 2. integer ends with either 1,4,6
def po4_trick(n):
    # n & (n - 1) == 0 make sure the number is power of 2
    # TODO: n % 10 extracts the LSB digit 
    return (n & (n - 1) == 0) and ((n % 10) in (1,4,6))

n = 128
sol = po4_trick(n)
print(sol)