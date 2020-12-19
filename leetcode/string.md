# String

+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s1 = list(s)
            t1 = list(t)
            s1.sort()
            t1.sort()
            for i in range(0, len(s1)):
                if s1[i] == t1[i]:
                    continue
                else:
                    return False  
            return True
        else:
            return False
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        s0 = [i for i in s]
        while i < j:
            if (s[i].lower() in 'aeiou') and (s[j].lower() in 'aeiou'):
                p = s0[j]
                s0[j] = s0[i]
                s0[i] = p
                i += 1
                j -= 1
            elif (s[i].lower() not in 'aeiou') and (s[j].lower() in 'aeiou'):
                i += 1
            elif (s[i].lower() in 'aeiou') and (s[j].lower() not in 'aeiou'):
                j -= 1
            elif (s[i].lower() not in 'aeiou') and (s[j].lower() not in 'aeiou'):
                i += 1
                j -= 1
        return ''.join(s0)
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s0 = s.split()
        for i in range(len(s0)):
            s1 = []
            s1 += s0[i]
            s1.reverse()
            s0[i] = ''.join(s1)
        return ' '.join(s0)
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
```