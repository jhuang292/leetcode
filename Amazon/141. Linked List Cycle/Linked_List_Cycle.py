# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hPointer = head
        while(True):
            if(head == None): break
            head = head.next
            if(hPointer == None or hPointer.next == None): break
            hPointer = hPointer.next.next
            if(head == hPointer): return True
            
        return False
        
