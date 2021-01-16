class MyLinkedList:

    def __init__(self, val=-1, nextnode=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = nextnode

    def __iter__(self):
        self.node = self
        return self

    def __next__(self):
        if self.node is not None:
            x = self.node.val
            self.node = self.node.next
            return x
        else:
            raise StopIteration

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        srcnode = self

        for _ in range(index):
            if srcnode is not None:
                srcnode = srcnode.next
            else:
                return -1
        if srcnode:
            return srcnode.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.val < 0:
            self.val = val
        else:
            self.val, self.next = val, MyLinkedList(self.val, self.next)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.val < 0:
            self.val = val
        else:
            srcnode = self
            while srcnode.next is not None:
                srcnode = srcnode.next
            srcnode.next = MyLinkedList(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        boolean = True
        srcnode = self

        if index > 0:
            for _ in range(index - 1):
                if srcnode is not None:
                    srcnode = srcnode.next
                else:
                    boolean = False
                    break

        if boolean:
            if index > 0:
                srcnode.next = MyLinkedList(val, srcnode.next)
            elif index == 0:
                if self.val == -1:
                    self.val = val
                else:
                    self.val, self.next = val, self

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        boolean = True
        srcnode = self

        if (index - 1) > 0:
            for _ in range(index - 1):
                if srcnode.next is not None:
                    srcnode = srcnode.next
                else:
                    boolean = False
                    break

        if boolean:
            if (index - 1) > 0:
                if srcnode.next:
                    srcnode.next = srcnode.next.next
            elif index == 1:
                if self.next:
                    self.next = self.next.next
            elif (index == 0) and (self.val != -1):
                if self.next:
                    self.val, self.next = self.next.val, self.next.next
                else:
                    srcnode = self.next


lst = MyLinkedList()
lst.addAtHead(3)
lst.addAtTail(5)
lst.addAtTail(7)

dup_of_lst = iter(lst)
print(next(dup_of_lst))
print(next(dup_of_lst))
print(next(dup_of_lst))
print('-----')
for num in lst:
      print(num)
print('-----')
for num in lst:
      print(num)