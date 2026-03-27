# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        pointerOne = list1
        pointerTwo = list2

        dummyNode = ListNode(0)
        headNode = dummyNode

        while(pointerOne and pointerTwo):
            if pointerOne.val < pointerTwo.val:
                headNode.next = pointerOne
                pointerOne = pointerOne.next
            else:
                headNode.next = pointerTwo
                pointerTwo = pointerTwo.next

            headNode = headNode.next
        
        while pointerOne:
            headNode.next = pointerOne
            pointerOne = pointerOne.next
            headNode = headNode.next

        while pointerTwo:
            headNode.next = pointerTwo
            pointerTwo = pointerTwo.next
            headNode = headNode.next

        return dummyNode.next