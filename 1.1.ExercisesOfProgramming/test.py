# coding:utf-8
# 全站排名 86,668


from requests import head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None
        slow, fast = head, head.next
        while fast.next and fast.next.next and fast != slow:
            slow = slow.next
            fast = fast.next.next 
        if fast.next and fast.next.next:
            lenA = 1
            node = slow.next
            while node != slow:
                lenA += 1
                node = node.next
            lenB = 0
            count = 0
            node = head
            while count < 2:
                lenB += 1
                node = node.next
                if node == slow:
                    count += 1
            res = head
            for _ in range(lenB-2*lenA-1):
                res = res.next
            return res
        else:
            return None

solo = Solution()
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2 
node2.next = node3 
node3.next = node4 
node4.next = node2
print(solo.detectCycle(node1).val)


