# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_prev, left_node = None, None
        prev = None
        curr = head
        cnt = 0

        while curr:
            cnt += 1

            if cnt == left:
                left_prev = prev
                left_node = curr
                tmp = curr.next

                while cnt <= right:
                    curr.next = prev
                    prev = curr
                    curr = tmp
                    if tmp:
                        tmp = tmp.next
                    cnt += 1

                if not left_prev:
                    left_node.next = curr
                    return prev
                else:
                    left_prev.next = prev
                    left_node.next = curr
                    return head

            prev = curr
            curr = curr.next