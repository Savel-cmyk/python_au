# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Binary Search Tree Iterator](#binary-search-tree-iterator)
+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)
+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Symmetric Tree](#symmetric-tree)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left = Solution().maxDepth(root.left)
        right = Solution().maxDepth(root.right)
        return max(left, right) + 1
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        lst = []
        lst += Solution().inorderTraversal(root.left)
        lst.append(root.val)
        lst += Solution().inorderTraversal(root.right)
        return lst
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        root.left = Solution().invertTree(root.left)
        root.right = Solution().invertTree(root.right)
        return root
```

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(src: TreeNode) -> TreeNode:
    if src == None:
        return []
    lst = []
    lst += inorderTraversal(src.left)
    lst.append(src.val)
    lst += inorderTraversal(src.right)
    return lst

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.list = inorderTraversal(root)
        self.nxt = -1

    def next(self) -> int:
        self.nxt += 1
        return self.list[self.nxt]

    def hasNext(self) -> bool:
        return (self.nxt + 2) <= len(self.list)
```

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while len(queue) > 0:
            for root in queue:
                level.append(root.val)
                if root.left != None:
                    next_queue.append(root.left)
                if root.right != None:
                    next_queue.append(root.right)
            result.append(level)
            queue = next_queue
            next_queue = []
            level = []
        return result
```

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(src: TreeNode) -> List[int]:
    if src == None:
        return []
    return inorder(src.left) + [src.val] + inorder(src.right)
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return inorder(root)[k - 1]
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(src: TreeNode) -> List[int]:
    return inorder(src.left) + [src.val] + inorder(src.right) if src != None else []
        
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root.left != None or root.right != None:
            lst = inorder(root)
            left = 0
            right = 1
            while right < len(lst):
                if lst[left] >= lst[right]:
                    return False
                left = right
                right += 1
        return True
```

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root]
        next_queue = []
        level = []
        src = TreeNode(-1)
        while queue != [] and root is not None:
            for curr in queue:
                level.append(curr.val)
                if curr.left == None:
                    next_queue.append(src)
                elif curr.left != None:
                    next_queue.append(curr.left)
                if curr.right == None:
                    next_queue.append(src)
                elif curr.right != None:
                    next_queue.append(curr.right)
            if level != list(reversed(level)):
                return False
            if level.count(-1) != len(level):
                queue = next_queue
            else:
                break
            next_queue = []
            level = []
        return True
```