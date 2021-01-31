# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        while head is not None:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node

# before we alter head we store in next_node
# point head to prev_node which starts as None then
# we set prev_node to head for next itertton
# Then we reset head back to its original so it points to the original next but prev_node holds the new next            
       
            
            

