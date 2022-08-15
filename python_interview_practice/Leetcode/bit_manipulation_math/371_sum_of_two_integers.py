# given two integers a and b, return the sum of the two integers without using the operators + and -

class Sol_sum:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def find_sum(self):
        a = self.a
        b = self.b
        # xor and &(for carry value)
        # 2 -> 0010, 3 -> 0011
        # 2 & 3 -> 0010 -> left shift one -> 00100
        # b is a & b. when a & b is 0, means no carry are possible, exit the loop
        while (b != 0):
            # want to calculate carry out using original a
            carry_out = (a & b) << 1
            a = a ^ b
            b = carry_out
        return a

if __name__ == "__main__":
    a = 2
    b = 3
    sol = Sol_sum(a,b)
    res = sol.find_sum()
    print(res)