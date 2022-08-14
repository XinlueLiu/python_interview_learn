
class Sol_reverse_bits:
    def __init__ (self, n):
        self.n = n
    def reverse_bits(self):
        res = 0
        # for the 32 bit range -> result 0-31
        for i in range(32):
            # get each bit of element by shifting the original number n to the right and AND with 1
            bit = (n >> i) & 1
            # assign the retrieved bit by left shifting (31-i) position and or with previous res
            res = res | (bit << (31-i))
        return res


if __name__ == "__main__":
    n = 964176192
    sol = Sol_reverse_bits(n)
    res = sol.reverse_bits()
    print(res)