# Array

+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = i = k = 0
        while i <= (len(nums) - 1):
            k = 0
            if nums[i] != 0: 
                while (nums[i] != 0) and (i < len(nums)):
                    k += 1
                    i += 1
                    if i >= len(nums): break
                if res < k:
                    res = k
                i += 1
            else:
                i += 1
        return res
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(nums[0]) * len(nums)) == (r * c):
            if (r != len(nums)) and (c != len(nums[0])):
                if len(nums) != 1:
                    for i in range(1, len(nums)):
                        for j in nums[i]:
                            nums[0].append(j)
                    del nums[1:]
                if r != 1:
                    while len(nums[0]) != c:
                        lst = []
                        for i in range(c, (2 * c)):
                            lst.append(nums[0][i])
                        del nums[0][c:(2 * c)]
                        nums.append(lst)
                return nums
        return nums
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if len(M) == len(M[0]) == 1:
            return M
        N = []
        for _ in range(len(M)):
            N.append([0 for _ in M[0]])
        for i in range(len(M)):
            for j in range(len(M[0])):
                if j == (len(M[0]) - 1) == 0:
                    if i == 0:
                        N[i][j] += (M[i][j] + M[(i + 1)][j]) // 2
                    elif i == (len(M) - 1):
                        N[i][j] += (M[i][j] + M[(i - 1)][j]) // 2
                    else:
                        N[i][j] += (M[i][j] + M[(i + 1)][j] + M[(i - 1)][j]) // 3
                elif j == 0:
                    if i == (len(M) - 1) == 0:
                        N[i][j] += (M[i][j] + M[i][(j + 1)]) // 2
                    elif i == 0:
                        N[i][j] += (M[i][j] + M[(i + 1)][j] + M[i][(j + 1)] + M[(i + 1)][(j + 1)]) // 4
                    elif i == (len(M) - 1):
                        N[i][j] += (M[i][j] + M[(i - 1)][j] + M[i][(j + 1)] + M[(i - 1)][(j + 1)]) // 4
                    else:
                        N[i][j] += (M[i][j] + M[(i + 1)][j] + M[i][(j + 1)] + M[(i + 1)][(j + 1)] + M[(i - 1)][(j + 1)] + M[(i - 1)][j]) // 6
                elif j == (len(M[0]) - 1):
                    if i == (len(M) - 1) == 0:
                        N[i][j] += (M[i][j] + M[i][(j - 1)]) // 2
                    elif i == 0:
                        N[i][j] += (M[i][j] + M[(i + 1)][j] + M[i][(j - 1)] + M[(i + 1)][(j - 1)]) // 4
                    elif i == (len(M) - 1):
                        N[i][j] += (M[i][j] + M[(i - 1)][j] + M[i][(j - 1)] + M[(i - 1)][(j - 1)]) // 4
                    else:
                        N[i][j] += (M[i][j] + M[(i - 1)][j] + M[i][(j - 1)] + M[(i - 1)][(j - 1)] + M[(i + 1)][(j - 1)] + M[(i + 1)][j]) // 6
                else:
                    if i == (len(M) - 1) == 0:
                        N[i][j] += (M[i][j] + M[i][(j - 1)]  + M[i][(j + 1)]) // 3
                    elif i == 0:
                        N[i][j] += (M[i][j] + M[(i + 1)][j] + M[i][(j - 1)] + M[(i + 1)][(j - 1)] + M[(i + 1)][(j + 1)] + M[i][(j + 1)]) // 6
                    elif i == (len(M) - 1):
                        N[i][j] += (M[i][j] + M[(i - 1)][j] + M[i][(j - 1)] + M[(i - 1)][(j - 1)] + M[(i - 1)][(j + 1)] + M[i][(j + 1)]) // 6
                    else:
                        N[i][j] += (M[i][j] + M[(i - 1)][j] + M[(i - 1)][(j + 1)] + M[i][(j + 1)] + M[(i + 1)][(j + 1)] + M[(i + 1)][j] + M[(i + 1)][(j - 1)] + M[i][(j - 1)] + M[(i - 1)][(j - 1)]) // 9
        return N
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            for j in range(((len(A[i]) - 1) // 2) + 1):
                A[i][j], A[i][~j] = A[i][~j] ^ 1, A[i][j] ^ 1
        return A
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        right = 0
        if len(A) > len(A[0]):
            right = len(A) - len(A[0])
            n = [0 for _ in range(len(A[0]), len(A))]
            for row in A:
                row += n
        elif len(A) < len(A[0]):
            right = len(A) - len(A[0])
            for _ in range(len(A), len(A[0])):
                A.append([0 for _ in range(len(A[0]))])
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        if right > 0:
            for i in range(right):
                del A[-1]
        elif right < 0:
            for row in A:
                del row[right::1]
        return A
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = False
        k = 0
        for obj in nums:
            if obj != 0:
                n = True
            else:
                k += 1
        if n:
            nums.insert(0, -1)
            for i in range((len(nums) - 1), 0, -1):
                if (nums[i] == 0) and (k != 0):
                    del nums[i]
                    nums.append(0)
                    k -= 1
                elif k == 0:
                    break
            del nums[0]
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)
```
