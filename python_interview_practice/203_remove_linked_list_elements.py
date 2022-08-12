
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Sol_remove_linked_list_elements:
    def __init__(self, head, target):
        self.head = head
        self.target = target
    def remove_element(self):
        head = self.head
        target = self.target
        # add a header dummy node to avoid corner case that head is the target
        dummy = ListNode(next = head)
        # maintain two pointers, prev and cur
        # when cur points to target value, prev.next = cur.next
        prev = dummy
        cur = head
        while(cur):
            if (cur.val == target):
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        # dummy node always points to the actual header, so return dummy.next
        return dummy.next

if __name__ == "__main__":
    node0 = ListNode(val = 1)
    node1 = ListNode(val = 2)
    node2 = ListNode(val = 6)
    node3 = ListNode(val = 3)
    node4 = ListNode(val = 4)
    node5 = ListNode(val = 5)
    node6 = ListNode(val = 6)
    target = 6
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    sol = Sol_remove_linked_list_elements(node0, target)
    res_head = sol.remove_element()
    while(res_head):
        print(res_head.val)
        res_head = res_head.next