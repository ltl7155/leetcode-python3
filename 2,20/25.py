# Definition for singly-linked list.
# 出现过很多错误，细节还是很多的
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # point = [50000]
        point = [0 for _ in range(50000)]
        if not head:
            return None

        begin = end = start = ListNode(0)
        start.next = head

        end = end.next
        while begin.next:
            for i in range(k):
                if not end:
                    return start.next
                point[i] = end
                end = end.next
            begin.next = point[k - 1]
            for i in range(0, k - 1):
                begin = begin.next
                begin.next = point[k - i - 2]
            begin = begin.next
            begin.next = end
        return start.next

l1 = ListNode(1)
l2 = ListNode(2)
# l3 = ListNode(3)
l1.next = l2
# l2.next = l3
s = Solution()
s.reverseKGroup(l1,1)