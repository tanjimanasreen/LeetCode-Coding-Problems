# Problem Link: https://leetcode.com/problems/linked-list-cycle


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Floyd's Hare and Tortoise Algorithm --> Optimized
        slow, fast = head, head

        while fast and fast.next:  # taking the fast object in case the list is empty
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

#         # Using Basic HashSet
#         hashSet = set()
#         pointer = head

#         while pointer and pointer.next:
#             if pointer in hashSet:
#                 return True

#             else:
#                 hashSet.add(pointer)
#                 pointer = pointer.next
#         return False
