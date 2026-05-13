# ── Length Difference Alignment ───────────────────────────
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_a = headA
        node_b = headB
        length_a = 0
        length_b = 0
        while node_a:
            node_a = node_a.next
            length_a += 1
        
        while node_b:
            node_b = node_b.next
            length_b += 1

        node_a = headA
        node_b = headB
        if length_a > length_b:
            while length_a > length_b:
                node_a = node_a.next
                length_a -= 1
        elif length_a < length_b:
            while length_a < length_b and node_b:
                node_b = node_b.next
                length_b -= 1
        while node_a:
            if node_a == node_b:
                return node_a
            node_a = node_a.next
            node_b = node_b.next
        return None

# Time Complexity:  O(m + n) — two passes to compute lengths and one pass to find intersection
# Space Complexity: O(1) — only a few pointer variables


# ── Two-Pointer Traversal ─────────────────────────────────
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pointer_a = headA
        pointer_b = headB
        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA
        return pointer_a

# Time Complexity:  O(m + n) — each pointer traverses at most m + n nodes
# Space Complexity: O(1) — only two pointer variables
