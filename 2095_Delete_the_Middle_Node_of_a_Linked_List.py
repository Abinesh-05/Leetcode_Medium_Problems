class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        y=head
        prev=head
        if head==None or not head.next:
            return None
        while(x and x.next):
            x=x.next.next
            prev=y
            y=y.next
        
        prev.next=y.next
        return head
