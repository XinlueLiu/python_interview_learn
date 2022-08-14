
def find_power_of_three(num):
    # power of 3
    # 1,3,9,27,81
    # so if keep dividing by 3, the last number should be 1
    # 6, for example. 6 -> 2 -> 0.xx, so will not pass the check
    if (num > 1):
        while(num % 3 == 0):
            num /= 3
    return num == 1

if __name__ == "__main__":
    num = 27
    res = find_power_of_three(num)
    print(res)