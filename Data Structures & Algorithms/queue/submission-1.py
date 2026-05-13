class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new = ListNode(value)

        new.next = self.tail
        temp = self.tail.prev
        temp.next = new
        new.prev = temp
        self.tail.prev = new

    def appendleft(self, value: int) -> None:
        new = ListNode(value)

        new.prev = self.head
        temp = self.head.next
        temp.prev = new
        new.next = temp
        self.head.next = new

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        temp = self.tail.prev
        temp2 = temp.prev
        temp2.next = self.tail
        self.tail.prev = temp2
        return temp.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        
        temp = self.head.next
        temp2 = temp.next
        temp2.prev = self.head
        self.head.next = temp2
        return temp.val
        
