class ListNode:
    def __init__(self, val = 0, nextNode = None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_node(self, val):
        newNode = ListNode(val)
        if (self.head == None):
            self.head = newNode
            return
        cur = self.head
        while(cur.nextNode != None):
            cur = cur.nextNode
        cur.nextNode = newNode
    
    def print_list(self):
        cur = self.head
        while(cur != None):
            print(f'{cur.val} ->')
            cur = cur.nextNode

class Sol_remove_duplicates:
    def __init__ (self, list1):
        self.list1 = list1
    
    def remove_duplicates_given_list(self):
        list1 = self.list1
        newList = LinkedList()
        cur = list1.head
        # manually add a case to avoid coner cases
        list1.insert_node(cur.val + 1)
        while(True):
            if (cur.nextNode == None):
                break
            tmpVal = cur.val
            cur = cur.nextNode
            if (tmpVal != cur.val):
                newList.insert_node(tmpVal)
        return newList

    def remove_duplicates_given_head_complicated(self, head):
        cur = head
        # if empty head, return None
        if (cur == None):
            return head
        # add a dummy tail node to avoid corner cases
        while True:
            if (cur.nextNode == None):
                dummyTailNode = ListNode()
                cur.nextNode = dummyTailNode
                break
            cur = cur.nextNode
        cur = head
        # traverse the linkedlist, keep to pointers points to prev and current node
        # if prev = current node, move prev.next = cur.next. Skip duplicated node
        # repeat until no more duplicated nodes are found
        while True:
            if (cur.nextNode == None):
                break
            prev = cur
            cur = cur.nextNode
            while (prev.val == cur.val):
                # corner case where from k to n nodes are all the same.
                if (cur.nextNode == None):
                    prev.nextNode = None
                    return head
                prev.nextNode = cur.nextNode
                cur = cur.nextNode
        cur = head
        # corner case consisting of the dummy tailnode
        while (cur.nextNode).nextNode != None:
            cur = cur.nextNode
        cur.nextNode = None
        return head

    def remove_duplicates_given_head(self, head):
        cur = head
        # while current node is not Null
        while cur:
            # while next node is not null and current value is not equal to next value
            while cur.nextNode and (cur.val == cur.nextNode.val):
                cur.nextNode = cur.nextNode.nextNode
            cur = cur.nextNode
        return head


if __name__ == '__main__':
    list1 = LinkedList()
    list1.insert_node(1)
    list1.insert_node(1)
    list1.insert_node(2)
    list1.insert_node(2)
    print(f'original list is :')
    list1.print_list()
    print(f'new distinct list if given the whole list is :')
    list2 = LinkedList()
    sol_remove_duplicates = Sol_remove_duplicates(list1)
    list2 = sol_remove_duplicates.remove_duplicates_given_list()
    list2.print_list()
    print(f'new distinct list if given the head of the list is :')
    newHeadNode = sol_remove_duplicates.remove_duplicates_given_head(list1.head)
    list3 = LinkedList(newHeadNode)
    list3.print_list()
