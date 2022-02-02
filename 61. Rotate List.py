Given the head of a linked list, rotate the list to the right by k places.
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 0:
            return head

        last = head
        count = 1
        while last.next:
            count +=1
            last = last.next

        #Making our last node pointing to the head
        last.next = head
        curr = head
        
        #Getting the place needed by K  
        for _ in range(count - (k%count) -1):
            curr = curr.next

        #Our new head
        #for K = 2, curr.next >> 4 so we're making it our head (result), and making the >> to None 
        result = curr.next
        curr.next = None
        
        return result
