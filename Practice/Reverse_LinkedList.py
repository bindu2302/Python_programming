class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def reverse_list(head):
    prev,curr = None,head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev,curr = curr,nxt
    return prev

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
new_head = reverse_list(head)

while new_head:
    print(new_head.val, end=" ->" if new_head.next else "\n")
    new_head= new_head.next