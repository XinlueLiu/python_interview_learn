

def find_power_of_two(x = 0):
    # for power of two values, the binary representation would be leading 1 following by zeros
    # 1->1, 2->10, 4->100, 8->1000, 16->10000
    return x > 0 and ((x & (x-1)) == 0)

if __name__ == "__main__":
    x = 1024
    res = find_power_of_two(x)
    print(res)