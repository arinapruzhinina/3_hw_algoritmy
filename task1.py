from typing import Optional

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: Optional[ListNode]) -> bool:
    arr, cur = [], head     
    while cur:              
        arr.append(cur.val) 
        cur = cur.next      
    return arr == arr[::-1] 