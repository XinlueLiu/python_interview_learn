class ListNode:
    def __init__ (self, x):
        self.val = x
        self.next = None

class Sol_intersection_of_two_linked_list_hash:
    def __init__ (self, headA, headB):
        self.headA = headA
        self.headB = headB

    def find_intersection(self):
        # add each element of headA to a list(hash)
        # then iterate through headB. First ListNode of listB that appears in ListA will be the intersection
        listA = []
        cur = self.headA
        while(cur):
            listA.append(cur)
            cur = cur.next
        cur = self.headB
        while(cur):
            if (cur in listA):
                return cur
            cur = cur.next
        return None

class Sol_intersection_of_two_linked_list:
    def __init__ (self, headA, headB):
        self.headA = headA
        self.headB = headB

    def find_intersection(self):
        l1 = self.headA
        l2 = self.headB
        # while l1 and l2 do not intersect
        while (l1 != l2):
            # if l1 is None, make it point to headB
            if (l1 == None):
                l1 = headB
            else:
                l1 = l1.next

            if (l2 == None):
                l2 = headA
            else:
                l2 = l2.next
        # if they intersect or both l1 and l2 are none
        # idea is that: headA has length of n, headB has length of m
        # then path of l1 is equal to path of l2 which is n+m
        # since they start from different startpoint, they will meet at beginning of smaller linked list after 1 round
        return l1

if __name__ == "__main__":
    node0_0 = ListNode(4)
    node0_1 = ListNode(1)
    node2 = ListNode(8)
    node3 = ListNode(4)
    node4 = ListNode(5)
    node1_0 = ListNode(5)
    node1_1 = ListNode(6)
    node1_2 = ListNode(1)
    # path 1
    node0_0.next = node0_1
    node0_1.next = node2
    # path 2
    node1_0.next = node1_1
    node1_1.next = node1_2
    node1_2.next = node2
    # common path
    node2.next = node3
    node3.next = node4
    
    sol = Sol_intersection_of_two_linked_list_hash(node0_0, node1_0)
    res = sol.find_intersection()
    if (res == None):
        print("no intersection")
    else:
        print(res.val)