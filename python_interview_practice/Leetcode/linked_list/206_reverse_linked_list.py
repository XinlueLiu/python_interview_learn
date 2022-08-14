class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class Sol_reverse_linked_list:
    def __init__ (self, head):
        self.head = head

    def reverse_list(self):
        head = self.head
        # maintain two pointers, prev and cur
        prev,cur = None, head
        while cur:
            # temporary node to hold cur.next variable
            nxt = cur.next
            cur.next = prev
            # shift the pointers 
            prev = cur
            cur = nxt
        # cur will point to Null this time, so prev is the new head
        return prev

if __name__ == "__main__":
    node0 = ListNode(val=1)
    node1 = ListNode(val=2)
    node2 = ListNode(val=3)
    node3 = ListNode(val=4)
    node4 = ListNode(val=5)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    cur = node0
    
    sol = Sol_reverse_linked_list(node0)
    res = sol.reverse_list()
    cur = res
    while(cur != None):
        print(cur.val)
        cur = cur.next