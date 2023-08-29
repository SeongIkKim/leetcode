# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    max_sum = 0
    cur_node = None

    def pairSum(self, head: Optional[ListNode]) -> int:
        self.cur_node = head
        def get_twin(node:ListNode) -> bool:
            if not node:
                return True
            check_pair_sum = get_twin(node.next)
            if check_pair_sum:
                self.max_sum = max(self.max_sum, self.cur_node.val + node.val)
                # 불필요한 재갱신 방지
                if self.cur_node.next == node:
                    check_pair_sum = False
                    return False
                else:
                    self.cur_node = self.cur_node.next
                    return True
        get_twin(head)
        return self.max_sum
            
                