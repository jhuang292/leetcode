# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # Define a node object
        self.nodes = []
        # Initialize the head and pointer iterator
        head = pointer = ListNode(0)
        
        # Iterate the item of lists
        for l in lists:
            # While it is the linkedlist
            while(l):
                # Node append all the values of the linkedlist
                self.nodes.append(l.val)
                # Update the iterator of linkedlist node
                l = l.next
                
        # Sort all the nodes elements
        for x in sorted(self.nodes):
                # Update pointer
                pointer.next = ListNode(x)
                pointer = pointer.next
        return head.next
