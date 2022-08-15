# reverse bits of a given 32 bits unsigned integer
# get the LSB, and or LSB to position(31-LSB)

def reverse_bits(x):
    res = 0
    for i in range(32):
        # get the LSB by shifting the digit of interest to LSB position and AND with 1
        LSB = (x >> i) & 1
        # shift LSB to position (31-i), then OR to original result
        res = res | (LSB << (31-i))
    return res

x = 4 # 100
sol = reverse_bits(x)
print(sol) 

# TODO: basic idea is to extra value of interest and shift to corresponding location
# extration: RIGHT shift bit of interest i times, i is the location of interested bit
# ORed: Or extrated bit to cumulated res. the extrated bit need to be left shifted to position(31-i)