# deque is a double ended queue that supports quicker append and pop operations
# FOR the appendleft and popleft function. append and pop will add/delete item in right most position
from collections import deque

class MyStack:
    def __init__(self):
        # create a deque
        self.q = deque()
    
    def push(self, x):
        # push to the right of deque
        self.q.append(x)

    def pop(self):
        # pop should remove the right most object(last in, but first out), 
        # but deque.popleft should remove left most object because its a FIFO. We should remove first element
        # so we loop through from index 0 until(but not include) the last element, and push each element back to the queue
        # then we pop the last element
        for i in range(len(self.q) - 1):
            num = self.q.popleft()
            # not self.q.push. It is MyStack object that has push method, not the queue
            self.push(num)
        return self.q.popleft()

    def top(self):
        # top for stack is the most recently added, which is the right most value
        # get the last value
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0

if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    param2 = myStack.top()
    param3 = myStack.pop()
    param4 = myStack.empty()
    print(f'param2 is {param2}, param3 is {param3}, param4 is {param4}')
