# 2095. Delete the Middle Node of a Linked List


# Approach:
# Find out length of ll then mid = n//2
# reach at mid node's prev and point its next to mid's next
# return head


# T.C = O(n)
# S.C = O(1)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return None

        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        
        mid = length // 2
        cnt = 1
        temp = head
        while temp != None and cnt != mid:
            cnt += 1
            temp = temp.next
        
        temp.next = temp.next.next

        return head
        
