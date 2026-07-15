class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        current = head
        visited = set()

        while current:

            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False