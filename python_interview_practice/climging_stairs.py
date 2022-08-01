

class Sol_climbing_chair:
    def __init__ (self, n):
        self.n = n

    def climb_chair(self):
        # we have the base cases that if n = 5, step 5 -> 5 is 0
        # step 4 -> 5 = 1, step 3 -> 5 = 2(1,1 or 2)
        # These three are the base case. 
        # Step 2 -> 5: if taking 1 step first, then we reach step 3, which we already know is gonna take 2 distinct ways
        # if taking 2 step first, then we reach step 4, which we already know is gonna take 1 distinct way to reach step 5
        # So for total of n stairs, 2 steps are already determined
        # The rest lower steps are determined by the previous two steps
        # We need n-2 culmulations to calculate total distinct ways
        num = self.n
        res = 0
        top_stair_minus_1 = 1
        top_stair_minus_2 = 2
        # special case. If input is less than 2, then without special treatment the result will be 2
        if (n == 1):
            return 1
        if (n == 0):
            return 0
        for steps in range(n-2):
            tmp = top_stair_minus_2
            top_stair_minus_2 = top_stair_minus_1 + top_stair_minus_2
            top_stair_minus_1 = tmp
        return top_stair_minus_2



if __name__ == '__main__':
    n = 2
    sol_climbing_chair = Sol_climbing_chair(n)
    res = sol_climbing_chair.climb_chair()
    print(f'numbers of distinct ways to climb to the top is {res}')
