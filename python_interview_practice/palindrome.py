
from tracemalloc import start


class Solution:
    def __init__(self,x):
        self.x = x

    def print_num(self):
        print(self.x)

    def find_palindrome(self):
        if (self.x < 0):
            print('False')
            return
        pal_list = list(map(int, str(self.x)))
        if (len(pal_list) == 1):
            print('True')
            return
        if (len(pal_list) % 2 == 0):
            start_index = int(len(pal_list) / 2)
            previous_index = start_index - 1
            for next_half_list in pal_list[start_index:]:
                if next_half_list == pal_list[previous_index]:
                    previous_index = previous_index - 1
                else:
                    print('False')
                    return
            print('True')
        else:
            start_index = int(len(pal_list) / 2) + 1
            previous_index = start_index - 2
            for next_half_list in pal_list[start_index:]:
                if next_half_list == pal_list[previous_index]:
                    previous_index = previous_index - 1
                else:
                    print('False')
                    return
            print('True')


if __name__ == '__main__':
    #this case!
    palindrome_solution = Solution(12321)
    palindrome_solution.find_palindrome()
