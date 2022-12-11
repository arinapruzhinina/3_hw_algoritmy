class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: ListNode) -> int:
    head_list = head               
    ans = ''                       
    while head_list:               
        ans += str(head_list.val)  
        head_list = head_list.next 
    return(int(ans,2))  