
class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next

class Sol_palindrome_linked_list:
    def __init__ (self, head):
        self.head = head

    def find_pl_list_reverse (self):
        # convert the linked list into an list, then see if its equal to its reverse
        # need extra memory
        nums = []
        while(self.head):
            nums.append(self.head.val)
            self.head = self.head.next
        new_num = nums[::-1]
        if (new_num == nums):
            return True
        else:
            return False 

    def find_pl_list_pointer(self):
        nums = []
        while(self.head):
            nums.append(self.head.val)
            self.head = self.head.next
        # maintain two pointers starts from left-most and right-most
        # while they do not cross each other, want to see if they are equal or not
        l,r = 0, len(nums) - 1
        while(l <= r):
            if (nums[l] != nums[r]):
                return False
            l += 1
            r -= 1
        return True

    def find_pl_linked_list_pointer(self):
        # maintain two pointers, a fast and a slow pointer
        # step1: fast move 2 steps a time, slow moves 1 step a time
        # when fast is None(even numbers) or fast.next is None(odd numbers), slow is at the middle
        # step2: reverse the second half of the list
        # step3: compare by two pointers point from two ends
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the linked list
        prev = None
        while(slow):
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # at the end, slow will be None and prev will be last element, the head of the reversed list
        l,r = self.head, prev
        while(r):
            if (l.val != r.val):
                return False
            r = r.next
            l = l.next
        return True

if __name__ == "__main__":
    node0 = ListNode(val=1)
    node1 = ListNode(val=2)
    node2 = ListNode(val=2)
    node3 = ListNode(val=1)
    node0.next = node1
    node1.next = node2
    node2.next = node3
    sol = Sol_palindrome_linked_list(node0)
    res = sol.find_pl_linked_list_pointer()
    print(res)