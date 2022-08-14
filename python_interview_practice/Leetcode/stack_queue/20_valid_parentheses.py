

class Solution_val_p:
    def __init__(self,s):
        self.s = s

    def find_vp(self):
        s = self.s
        # Can use a stack-like structure
        # first character must be open brackets
        # so we can create a dict with key being close brackets, values being open brackets
        # loop through the original list. If open brackets, push to the stack
        # If encounter a close stack, check if the corresponding open bracket is at the end of list(top of stack)
        # If so, pop the open bracket. Else return false
        # For example, ({[]}) is valid. We push ({[ first, then encounter]}), which we pop corresponding value
        # {[}] is not valid. after {[, when we encounter }, we realize correspoding open bracket of { is not top of the list
        stack = []
        lookup_table = {')':'(', '}':'{', ']':'['}
        for each_item in s:
            # check if each_item is a key(if it is one of the closing brackets)
            if each_item in lookup_table:
                # check if the corresponding value(opening bracket) is the top of the list
                # if stack has at least one element(start with open brackets)
                if stack and (lookup_table[each_item] == stack[-1]):
                    stack.pop()
                else:
                # if stack is empty, and trying to start with a closed bracket
                # if corresponding value is NOT on top of the list
                    return False
            else:
                stack.append(each_item)
        if (len(stack) == 0):
            return True
        else:
            return False



if __name__ == '__main__':
    sol = Solution_val_p("([{}])")
    val_p_sol = sol.find_vp()
    print(f'solution of valid parentheses problem is {val_p_sol}')