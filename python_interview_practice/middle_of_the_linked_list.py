class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

def find_middle(head):
    # two pointers
    # slow one move 1 step, fast one move 2 steps
    # once fast one is Null(even), or fast one .next is Null(odd), return slow pointer
    # slow pointer will be the middle point
    slow,fast = head,head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow
    

if __name__ == "__main__":
    node0 = ListNode(val=1)
    node1 = ListNode(val=2)
    node2 = ListNode(val=3)
    node3 = ListNode(val=4)
    node4 = ListNode(val=5)
    node5 = ListNode(val=6)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    sol = find_middle(node0)
    cur = sol
    while(cur != None):
        print(cur.val)
        cur = cur.next