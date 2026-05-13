class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        count = 0
        curr = self.head.next
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        curr = ListNode(val)
        curr.next = self.head.next
        self.head.next = curr
        #did not get this last line: if list was empty before
        if not curr.next:
            self.tail = curr

    def insertTail(self, val: int) -> None:
        curr = ListNode(val)
        self.tail.next = curr
        self.tail = curr

    def remove(self, index: int) -> bool:
        count = 0
        curr = self.head
        
        while count < index and curr:
            curr = curr.next
            count += 1

            #curr is the one we are currently at and is the one before
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
                curr.next = None
                return True
            curr.next = curr.next.next
            return True
        return False
        



    def getValues(self) -> List[int]:
        curr = self.head.next
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return(ans)

