# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        # create a new linked list to hold the merged result
        result = ListNode()
        curr = result

        # while list1 and list2 is not None
        while list1 and list2:
            # built method "val" from "ListNode"
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

            # add any remaining nodes from list1 or list2
            if list1 or list2:
                curr.next = list1 if list1 else list2

        # result variable as a starting point for the merged list, but we don't modify it directly.
        # Instead, we use a separate pointer curr to keep track of the last node in the merged list
        # and build up the list by appending new nodes to curr.next
        return result.next


def main():
    # create a sorted list: 1 -> 2 -> 3 -> 4 -> 5
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # create a sorted list: 1 -> 4 -> 6 -> 7 -> 9
    head2 = ListNode(1, ListNode(4, ListNode(6, ListNode(7, ListNode(9)))))

    solution = Solution()

    # merge two lists into one using the mergeTwoLists method
    merged_head = solution.mergeTwoLists(head1, head2)

    # print the values of the nodes in the merged list
    while merged_head:
        print(merged_head.val)
        merged_head = merged_head.next


if __name__ == '__main__':
    main()
