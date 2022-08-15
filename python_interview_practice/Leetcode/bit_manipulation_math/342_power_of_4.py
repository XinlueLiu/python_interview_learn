
def find_power_of_4(n):
    # can either loopa and modulo, check if final result is 1
    # or use the trick that power of 4 need to be power of 2, so n&(n-1) must be 0
    # and power of 4 should end the last digit with either 1,4,or 6
    #1,4,16,64,256
    return ((n & (n-1)) == 0) and ((n % 10) in (1,4,6))

if __name__ == "__main__":
    num = 64
    res = find_power_of_4(num)
    print(res)