class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        original = []

        current = head
        while current:
            original.append(current.val)
            current = current.next

        # Reverse the linked list
        current = head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        reversed_list = []

        current = prev
        while current:
            reversed_list.append(current.val)
            current = current.next

        return original == reversed_list