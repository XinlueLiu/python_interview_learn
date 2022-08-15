# given an integer x, return true if x is palindrome integer

def find_palindrome(x):
    # negative number is not palindrome
    if (x < 0):
        return False
    # palindrome number is equal to its reverse
    # convert original value to a list. need str because int is not iterable
    x_reverse = list(str(x))
    # reverse reverse in-place, but [::-1] returns a new reversed list
    # non the less, they reverse the list and compare if the reverse one is equal to the original one
    x_reverse.reverse()
    if (x_reverse == list(str(x))):
        return True
    else:
        return False

x = 10
sol = find_palindrome(x)
print(sol)

# TODO: list need to take a iteratble variable. int is not iterable
# compare the original list with the reversed list