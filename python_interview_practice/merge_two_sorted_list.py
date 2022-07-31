class ListNode:
    def __init__ (self, val = 0, nextNode = None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    def __init__ (self, head = None):
        self.head = head

    def insert(self, value):
        # create new node
        new_node = ListNode(value)
        # if empty linked list, make the new_node being the head
        if (self.head == None):
            self.head = new_node
            return
        # create a pointer to point to the head of the linked list
        cur_node = self.head
        # traverse the linked list. If reach the end of the list, insert the new_node 
        while True:
            if (cur_node.nextNode == None):
                cur_node.nextNode = new_node
                break
            cur_node = cur_node.nextNode

    def print_list(self, listname):
        # create a pointer to point to the head of the linked list
        cur_node = self.head
        # traverse the linked list and print each element
        print(f'listname : {listname}')
        while(cur_node != None):
            print(f'{cur_node.val} ->')
            cur_node = cur_node.nextNode
        print(f'EOL')

class Sol_merge_two_sorted_list:
    def __init__ (self, list1_head, list2_head):
        self.list1_head = list1_head
        self.list2_head = list2_head

    def merge_two_sorted_list(self):
        list1_head = self.list1_head
        list2_head = self.list2_head
    
        # construct a dummy head
        sol_list_head = ListNode()
        # create current pointer to point to the head
        cur = sol_list_head
        # cconstruct a new linked list with dummy head to avoid edge cases
        sol_list = LinkedList(sol_list_head)
    
        # while two lists are not empty
        # insert smaller value to the sol_list and move the pointer of the inserted list
        while list1_head and list2_head:
            if list1_head.val > list2_head.val:
                sol_list.insert(list2_head.val)
                list2_head = list2_head.nextNode
            else:
                sol_list.insert(list1_head.val)
                list1_head = list1_head.nextNode
            # increment the current list
            cur = cur.nextNode

        # after exhausting one of the list, insert the rest list to the end of the sol_list
        if (list1_head):
            cur.nextNode = list1_head
        elif (list2_head):
            cur.nextNode = list2_head

        # update the list without the dummy listhead
        sol_list_head = sol_list_head.nextNode
        sol_list = LinkedList(sol_list_head)

        return sol_list
    


if __name__ == '__main__':
    list1 = LinkedList()
    list2 = LinkedList()
    list1.insert(1)
    list1.insert(2)
    list1.insert(4)
    list1.insert(6)
    list1.insert(7)
    list1.insert(8)
    list1.print_list('list1')
    list2.insert(1)
    list2.insert(3)
    list2.insert(4)
    list2.print_list('list2')
    sol = Sol_merge_two_sorted_list(list1.head, list2.head)
    sol_list = sol.merge_two_sorted_list()
    sol_list.print_list('sol_list')