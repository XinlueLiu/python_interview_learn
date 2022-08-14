class ListNode:
    def __init__ (self,x):
        self.val = x
        self.next = None

class Sol_linked_list_cycle_hash:
    def __init__ (self, head):
        self.head = head

    def find_cycle(self):
        # a list but instead of hash the value, we hash the node itself 
        list_node = []
        cur = self.head
        while(cur != None):
            # check if the node is already in the list. If it is than return ture
            if (cur in list_node):
                return True
            list_node.append(cur)
            cur = cur.next
        # if we have exhauste the entire list and has not found the node, return false
        return False

class Sol_linked_list_cycle_fast:
    def __init__ (self, head):
        self.head = head

    def find_cycle(self):
        slow, fast = self.head, self.head
        # since fast ptr goes 2 steps at a time, need to make sure both fast and fast.next not None
        while(fast and fast.next):
            # if total linked list length is n, then distance between fast and slow is n-1 for the first step
            # then the distance will becomes n-1-2+1 = n-1-1, so eventually n-1 will become 0 and they meed
            # So the time complexity is O(n) and fast and slow pointer will eventually meet
            slow = slow.next
            fast = fast.next.next
            if (fast == slow):
                return True
        return False

if __name__ == '__main__':
    newNode0 = ListNode(3)
    newNode1 = ListNode(2)
    newNode2 = ListNode(0)
    newNode3 = ListNode(-4)
    newNode0.next = newNode1
    newNode1.next = newNode2
    newNode2.next = newNode3
    newNode3.next = newNode1

    # print the linkedlist
    # cur = newNode0
    # while(cur != None):
    #     print(f'{cur.val} ->')
    #     cur = cur.next

    sol = Sol_linked_list_cycle_hash(newNode0)
    res = sol.find_cycle()
    print(f'it is {res} that there is a cycle in the linkedlist')

    