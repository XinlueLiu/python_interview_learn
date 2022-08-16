import math

class Sol_sqrt_x:
    def __init__ (self, x):
        self.x = x
    
    def sqrt(self):
        # use built-in math function
        # return math.sqrt(x)
        # can use binary search. Because square is to find a number n, such that n^2 is x
        lo, hi = 0, x
        while lo <= hi:
            # floor division
            mid = (lo + hi) // 2
            if (mid * mid > x):
                hi = mid - 1
            elif (mid * mid < x):
                lo = mid + 1
            else:
                # if have a square root
                return mid
        # if there is no perfect square root, return lo if round up, hi if round down
        return hi
            # 8
            # lo = 0, hi = 8, mid = 4
            # lo = 0, hi = 3, mid = 1
            # lo = 1, hi = 3, mid = 2
            # lo = 2, hi = 3, mid = 2
            # lo = 3, hi = 3, mid = 4
            # lo = 3, hi = 2, exit. low has crossed hi

if __name__ == "__main__":
    x = 5
    sol = Sol_sqrt_x(x)
    res = sol.sqrt()
    print(res)