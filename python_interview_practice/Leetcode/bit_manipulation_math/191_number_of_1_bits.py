
class Sol_number_of_1_bits:
    def __init__ (self, x):
        self.x = x
        
    def find_num_1(self):
        x = self.x
        # first method is to AND the LSB of x with 1, and accumulate the result
        res = 0
        while(x != 0):
            res = res + (x & 1)
            # update x by elimitating its LSB
            x = x >> 1
        return res

    def find_num_1_efficient(self):
        # AND x with (x-1). x-1 is essentially eliminating right most 1 and change 0s right of that 1 to be 1
        # when we AND original x with (x-1), 1s left of right most 1 will be ANDing with itself, 
        # 0s right of right most of 1 will be anding with 1s
        # we we are getting rid of one right most 1 at a time
        x = self.x
        res = 0
        while(x != 0):
            x &= (x-1)
            res += 1
        return res

if __name__ == "__main__":
    x = 9
    sol = Sol_number_of_1_bits(x)
    res = sol.find_num_1()
    print(res)