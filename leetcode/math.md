#Math

+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
class Solution:
    def reverse(self, x: int) -> int:
        if -2**31 <= x <= (2**31)-1:
            y = x
            x = 0
            if y < 0:
                y = -y
                while y != 0:
                    x = (x * 10) + (y % 10)
                    y = y // 10
                if -2**31 <= x <= (2**31)-1:
                    return -x
                else:
                    return 0
            elif y > 0: 
                while y != 0:
                    x = (x * 10) + (y % 10)
                    y = y // 10
                if -2**31 <= x <= (2**31)-1:
                    return x
                else:
                    return 0
            else:
                return 0
        else:
            return 0
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x <= (2**31)-1:
            z = y = x
            x = 0
            if y < 0:
                return False
            elif y > 9: 
                while y != 0:
                    x = (x * 10) + (y % 10)
                    y = y // 10
                return x == z
            else:
                return True
        else:
            return False
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        p = []
        for i in range (1, (n + 1)):
            if i % 15 == 0:
                p += ["FizzBuzz"]
            elif i % 5 == 0:
                p += ["Buzz"]
            elif i % 3 == 0:
                p += ["Fizz"]
            else:
                p += [str(i)]
            i += 1
        return p
```

## Base 7

https://leetcode.com/problems/base-7/

```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        p = ""
        if num < 0:
            num = -num
            while num != 0:
                p += str(num % 7)
                num = num // 7
            l = len(p)
            h = list(p)
            p = ""
            h.reverse()
            for i in range(0, l):
                p += h[i]
            return ('-' + p)
        elif num > 0:
            while num != 0:
                p += str(num % 7)
                num = num // 7
            l = len(p)
            h = list(p)
            p = ""
            h.reverse()
            for i in range(0, l):
                p += h[i]
            return p
        else:
            return "0"
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
class Solution:
    def fib(self, N: int) -> int:
        import numpy as np
        arr = np.zeros(32)
        arr[1] = 1
        if N <= 1:
            return N
        else:
            for i in range(2, (N + 1)):
                arr[i] = arr[i - 1] + arr[i - 2]
            return int(arr[N])
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        res = 0
        A.sort()
        for i in range(0, len(A)-2):
            if (A[i] + A[i + 1] > A[i + 2]) and (res < A[i] + A[i + 1] + A[i + 2]):
                res = A[i] + A[i + 1] + A[i + 2]
        return res
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        x = x ** 0.5
        return int(x)
```