# Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input:
# l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output:
# [7, 0, 8]
# Explanation:
# 342 + 465 = 807

# Example 2:
# Input:
# l1 = [0], l2 = [0]
# Output:
# [0]

# Example 3:
# Input:
# l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# Output:
# [8, 9, 9, 9, 0, 0, 0, 1]

# Constraints:
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    # insert in reverse order
    def insert_beginning(self, values):
        for val in values:
            node = Node(int(val))
            node.next = self.head
            self.head = node

    # to insert the digit of the result list
    def insert_end(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            ptr = self.head
            while ptr.next:
                ptr = ptr.next
            ptr.next = node

    def display(self):
        ptr = self.head
        while ptr:
            print(ptr.val, ", ", end="")
            ptr = ptr.next
        print()

def add_two_numbers(l1, l2):
    l1_ptr = l1.head
    l2_ptr = l2.head
    result = SinglyLL()
    carry = 0

    while True:
        if not l1_ptr and not l2_ptr: # when no digits remaining in both lists
            break

        elif not l1_ptr: # when no digits remaining in l1 but in l2
            sum = l2_ptr.val + carry
            l2_ptr = l2_ptr.next
        
        elif not l2_ptr: # when no digits remaining in l2 but in l1
            sum = l1_ptr.val + carry
            l1_ptr = l1_ptr.next
        
        else: # digit available in both lists
            sum = l1_ptr.val + l2_ptr.val + carry
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next

        # determine if carry occurs or not in addition 
        if sum/10 >= 1:
            result.insert_end(sum % 10)
            carry = 1
        else:
            result.insert_end(sum)
            carry = 0
    
    # carry overflow
    if carry == 1:
        result.insert_end(carry)

    return result

if __name__ == "__main__":
    l1 = SinglyLL()
    l2 = SinglyLL()
    result = SinglyLL()

    num = input("l1: ")
    l1.insert_beginning(num)

    num = input("l2: ")
    l2.insert_beginning(num)

    l1.display()
    l2.display()

    result = add_two_numbers(l1, l2)
    result.display()
