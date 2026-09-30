# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(-1)
        head = temp = dummy

        curr1, curr2 = list1, list2
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                temp.next = curr1
                temp = temp.next
                curr1 = curr1.next

            else:
                temp.next = curr2
                temp = temp.next
                curr2 = curr2.next

        if curr2:
            temp.next = curr2

        if curr1:
            temp.next = curr1

        return head.next
           
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
            
        def rec(low, high):
            if low == high:
                return lists[low]

            mid = low + (high - low + 1) // 2
            left = rec(low, mid-1)
            right = rec(mid, high)
            return self.merge(left, right)

        return rec(0, len(lists) - 1)