# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        results = [[0 for i in range(n)] for i in range(m)]
        top, left = 0, 0
        bottom, right = m-1, n-1 

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                if head:
                    results[top][i] = head.val
                    head = head.next
                else:
                    results[top][i] = -1
            top += 1

            for i in range(top, bottom+1):
                if head:
                    results[i][right] = head.val
                    head = head.next
                else:
                    results[i][right] = -1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    if head:
                        results[bottom][i] = head.val
                        head = head.next
                    else:
                        results[bottom][i] = -1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top-1, -1):
                    if head:
                        results[i][left] = head.val
                        head = head.next
                    else:
                        results[i][left] = -1
                left += 1
        
        return results
