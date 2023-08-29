# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        가능하다면 recursive를 통한 콜스택 호출을 삼갈 것
        """
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next # after then slow is middle
        
        cur, prev = slow, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next # after then prev is last node
        
        former, latter = head, prev
        max_sum = 0
        while latter: # or former
            max_sum = max(max_sum, former.val + latter.val)
            former, latter = former.next, latter.next

        return max_sum

        
            
                