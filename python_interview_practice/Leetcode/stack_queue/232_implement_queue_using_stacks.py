# queue is FIFO. add item to the right of deque(last) and remove the left most element(the earlist added)
# Stack is LIFO. add item to the right of deque(last) and remove the right most element(the most recently added)

from collections import deque

class myQueue:
    def __init__ (self):
        # maintain two queues. q1 is the queue with real content
        # q2 is the queue to help perform pop operation
        self.q1 = deque()
        self.q2 = deque()

    def push(self,x):
        # just push onto the queue
        self.q1.append(x)

    def pop(self):
        # since its stack, we can only pop the most recently added, aka deque().pop method
        # pop every item in q1 except last one(first one pushed onto the queue), and push every 
        # item onto another queue(q2)
        # the left item will be the item to be poped as a queue. Then push every item on q2 back to q1
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop())
        res = self.q1.pop()
        for i in range(len(self.q2)):
            self.q1.append(self.q2.pop())
        return res
    
    def peek(self):
        # return the first element onto the queue
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

    def debug_print(self):
        print(f'q1 element is {self.q1}')
        print(f'q2 element is {self.q2}')

if __name__ == "__main__":
    myQ = myQueue()
    myQ.push(1)
    myQ.push(2)
    myQ.push(3)
    myQ.push(4)
    myQ.peek() # should return 4
    res = myQ.pop()
    print(res) # should return 4
    res = myQ.empty()
    print(res) # should return False
    myQ.debug_print()