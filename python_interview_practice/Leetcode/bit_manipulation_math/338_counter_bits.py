
# given an integer n, return an array ans of length n + 1 such that for each i, ans[i] is the 
# number of 1's in the binary representation of i
# n = 2 -> 0,1,2 -> 0,1,10 -> [0,1,1]

class Sol_counter_bits:
    def __init__(self, n):
        self.n = n
    def count_bits(self):
        res = []
        # for each value from 0 to n, convert it to binary representation, sum each bit(number of 1's)
        for i in range(self.n + 1):
            # bin will return a string with leading 0b, I want a integer list that discard 0b
            # map each iterable bin[2:]
            bin_list = list(map(int, bin(i)[2:]))
            res.append(sum(bin_list))
        return res

if __name__ == "__main__":
    n = 5
    sol = Sol_counter_bits(n)
    res = sol.count_bits()
    print(res)