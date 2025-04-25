# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(node):
            if not node or not node.next:
                return node
            
            fast = slow = node
            prev = None
            while fast and fast.next:

                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None
            right = merge_sort(slow)
            left = merge_sort(node)
            return merge(left,right)

        def merge(left,right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            if left:
                tail.next = left
            if right:
                tail.next = right
            return dummy.next
            
        return merge_sort(head)

        
