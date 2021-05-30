# Linked-list

+ [Reverse Linked List](#reverse-linked-list)
+ [Middle of the Linked List](#middle-of-the-linked-list)
+ [Palindrome Linked List](#palindrome-linked-list)
+ [Merge Two Sorted Lists](#merge-two-sorted-lists)
+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)
+ [Linked List Cycle II](#linked-list-cycle-ii)
+ [Linked List Cycle](#linked-list-cycle)
+ [Reorder List](#reorder-list)
+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)
+ [Sort List](#sort-list)
+ [Merge k Sorted Lists](#merge-k-sorted-lists)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        k = 0
        curr = head
        while curr != None:
            k += 1
            curr = curr.next
        k = (k // 2) + 1
        for _ in range((k - 1)):
            head = head.next
        return head
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        for i in range((len(lst) // 2)):
            if lst[i] != lst[-(i + 1)]:
                return False
        return True
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        sorted_list = ListNode()
        cur = sorted_list

        while l1 is not None and l2 is not None:
            if l1.val < l2.val :
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1

        return sorted_list.next
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = prev = head
        bool = False
        while cur:
            if n == 0:
                cur = cur.next
                n -= 1
                bool = True
            elif n != -1:
                cur = cur.next
                n -= 1
            else:
                prev = prev.next
                cur = cur.next
        try:
            if bool:
                prev.next = prev.next.next
            else:
                head = head.next
        except AttributeError:
            head = None
        return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head
        lookup = set()

        while cur:
            if cur in lookup:
                return cur
            lookup.add(cur)
            cur = cur.next
        return None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        curr = head
        k = 1
        while (curr != None) and (curr.next != None):
            curr = curr.next
            k += 1
        prev = stat = head
        for i in range(k // 2):
            stat = stat.next
        for i in range(((k - 1) // 2)):
            curr = stat
            for n in range(((k - 1) // 2) - (i + 1)):
                curr = curr.next
            print(prev.val, curr.val)
            curr.next.next, curr.next, prev.next = prev.next, None, curr.next
            prev = prev.next.next
        return head
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lookup = set()
        while headB != None:
            lookup.add(headB)
            headB = headB.next
        while headA != None:
            if headA in lookup:
                return headA
            headA = headA.next
        return headA
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        if len(lst) > 0:
            lst.sort()
            head = ListNode(lst[0])
            curr = head
            del lst[0]
            for val in lst:
                curr.next = ListNode(val)
                curr = curr.next
        return head
```

## Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists and (len(lists) == 0):
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (1 + i) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        sorted_list = ListNode()
        curr = sorted_list
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1 is None:
            curr.next = l2
        elif l2 is None:
            curr.next = l1
            
        return sorted_list.next
```