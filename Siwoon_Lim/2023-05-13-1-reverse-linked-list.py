class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # check head list is empty
        if head is None:
            return None

        # check head list is only one value
        elif head.next is None:
            return head
        # store head list value into previous
        prev = head
        # store head list next value into current
        curr = prev.next
        # store current next value (head list next, next value) into temp
        temp = curr.next
        prev.next = None

        # if temp is not none
        while temp:
            # reverse current next value retrieving from previous value
            curr.next = prev
            # keep change from previous to temp
            prev = curr
            curr = temp
            temp = temp.next
        # change last node value from previous value
        curr.next = prev
        return curr


def main():
    # create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    solution = Solution()

    # reverse the linked list using the reverseList method
    reversed_head = solution.reverseList(head)

    # print the values of the nodes in the reversed linked list
    while reversed_head:
        print(reversed_head.val)
        reversed_head = reversed_head.next


if __name__ == '__main__':
    main()
