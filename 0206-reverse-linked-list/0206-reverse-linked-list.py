# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        previous = None
        current = head

        while current:

            nxt = current.next      # next node save

            current.next = previous # reverse

            previous = current      # move previous

            current = nxt           # move current

        return previous