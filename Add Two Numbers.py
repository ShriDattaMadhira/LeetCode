"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1, list2, list3 = "", "", ""
        while l1 != None:
            list1 += str(l1.val)
            l1 = l1.next

        while l2 != None:
            list2 += str(l2.val)
            l2 = l2.next

        print(list1, list2)
        list3 = str(int(list1[::-1]) + int(list2[::-1]))[::-1]
        print(list3)
        l3 = ListNode(list3[0], None)
        prev = l3
        for num in list3[1:]:
            temp = ListNode()
            temp.val = int(num)
            temp.next = None
            prev.next = temp
            prev = temp
        return l3