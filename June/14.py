# 2130. Maximum Twin Sum of a Linked List


# Approach:
# Here we have to return the maximum twin sum we can get.
# twin = ith --> (n-1-i)th
# i have added all val in a list
# applied 2 pointer and stored maximum twin sum
# and returned maxtsum

# T.C = O(n)
# S.C = O(n)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        li = []
        temp = head

        while temp != None:
            li.append(temp.val)
            temp = temp.next
        
        l = 0
        r = len(li)-1
        maxtsum = 0

        while l < r:
            tsum = li[l] + li[r]
            maxtsum = max(maxtsum, tsum)
            l += 1
            r -= 1
        
        return maxtsum
        