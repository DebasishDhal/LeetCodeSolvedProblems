'''
#Medium level
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 2+5=7,4+6=10(1 carried over), 3+4 +1(carry) = 8

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(val = 0)
        current = dummy_head
        carry = 0 #For carrying over the remainder to the next value

        while l1 or l2 or carry:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry #Carry from the previous ieration
            carry, remainder = divmod(total, 10)

            current.next = ListNode(remainder) #Remainder gets attached to the current node
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next #returning dummy_head.next because we haven't added anything to dummy_head itself.
