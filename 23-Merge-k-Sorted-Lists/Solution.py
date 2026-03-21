# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        heap = []
        dummyNode = ListNode(0)
        currentNode = dummyNode
        count = 0

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1
        
        while heap:
            val, _, smallestNode = heapq.heappop(heap)
            currentNode.next = smallestNode
            currentNode = currentNode.next

            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, count, smallestNode.next))
                count += 1
        
        return dummyNode.next

        # if (len(lists) == 0):
        #     return None

        # dummyNode = ListNode(0)
        # currentNode = dummyNode
        # count = 0

        # minHeap = []
        
        # for listHead in lists:
        #     if listHead:
        #         heapq.heappush(minHeap, (listHead.val, count, listHead))
        #         count += 1

        # while minHeap:
        #     val, _, newNode = heapq.heappop(minHeap)
        #     currentNode.next = newNode
        #     currentNode = currentNode.next

        #     if newNode.next:
        #         heapq.heappush(minHeap, (newNode.next.val, count, newNode.next))
        #         count += 1
        
        # return dummyNode.next
        