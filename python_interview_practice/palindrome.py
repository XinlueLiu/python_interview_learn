
from tracemalloc import start

class slicing_instr:
    def __init__(self, x):
        self.x = x
        print(f'the original list is {x}')
        # slicing 
        print(f'a[start:stop] item start through stop with default step 1 x[1:4] : {x[1:4]} -> stop value is not included')
        print(f'a[start:] item start through the rest of the array: {x[1:]}')
        print(f'a[:stop] item stop from beginning to stop-1: {x[:4]}')
        print(f'a[:] copy form the whole array: {x[:]}')
        print('Remember, STOP represent that first value that is NOT in the selected slice')
        print(f'a[::-1]: all item in the array REVERSED {x[::-1]}')

class Solution_simple:
    def __init__(self, num):
        self.num = num
        print(f'the value is {num}')
    
    def find_palindrome(self):
        if (self.num < 0):
            print('False')
        # convert the number to a list
        pal_list = list(map(int, str(self.num)))
        print(f'the new list constructed from input int is {pal_list}')
        # reverse the list 
        reversed_list = pal_list[::-1]
        print(f'the reversed list is {reversed_list}')
        # number is a palindrome if (pal_list == reversed_list) 
        if pal_list == reversed_list:
            print("True")
        else:
            print("False")

class Solution_ptr:
    def __init__(self,x):
        # define attribute x to be x
        self.x = x

    def print_num(self):
        print(self.x)

    def find_palindrome(self):
        # negative numbers cannot be palindrome
        if (self.x < 0):
            print('False')
            return
        # map() function process all items in an iterable without using loop
        # map() takes a function object and an iterable as argument
        pal_list = list(map(int, str(self.x)))
        print(f'pal_list is {pal_list}, length is {len(pal_list)}')
        # a single digit number is automatically a palindrome
        if (len(pal_list) == 1):
            print('True')
            return
        # if it is even number of digits
        if (len(pal_list) % 2 == 0):
            # assign start_index and previous_index starting from middle of the list
            start_index = int(len(pal_list) / 2)
            previous_index = start_index - 1
            # start traverse the list from start_index to the end of the list
            # if not the same, NOT palindrome
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
            # skip the value in the middle and traverse the list
            for next_half_list in pal_list[start_index:]:
                if next_half_list == pal_list[previous_index]:
                    previous_index = previous_index - 1
                else:
                    print('False')
                    return
            print('True')


if __name__ == '__main__':
    # palindrome_solution = Solution_ptr(12321)
    palindrome_solution = Solution_simple(12321)
    palindrome_solution.find_palindrome()
    slicing_instr([0,1,2,3,4])
