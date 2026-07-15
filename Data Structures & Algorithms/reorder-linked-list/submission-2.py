class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.front = head
        self.done = False

        def recurse(node):
            if node is None:
                return
            recurse(node.next)

            if self.done or self.front is None:
                return

            if self.front == node:
                self.front.next = None
                self.done = True
                return

            if self.front.next == node:
                self.front.next = node
                node.next = None
                self.done = True
                return

            tmp = self.front.next
            self.front.next = node
            node.next = tmp
            self.front = tmp

        recurse(head)