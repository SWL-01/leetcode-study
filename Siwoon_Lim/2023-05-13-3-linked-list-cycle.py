# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # visited set
        v = set()
        # if head is none, the link is ended -> no cycle
        while head:
            # if head is in visited set, there is cycle
            if head in v:
                return True
            # mark every state which is visited
            else:
                v.add(head)
                head = head.next
        return False


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Cycle
    head.next.next.next.next.next = head.next.next

    solution = Solution()

    has_cycle = solution.hasCycle(head)

    # print whether the linked list has a cycle or not
    if has_cycle:
        print("True.")
    else:
        print("False.")


if __name__ == '__main__':
    main()
