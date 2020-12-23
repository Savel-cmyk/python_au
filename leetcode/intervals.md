# Intervals

+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(len(intervals)):
            for j in range((i + 1), len(intervals)):
                if intervals[i][0] == intervals[j][0]:
                    if (intervals[i][1] - intervals[i][0]) < (intervals[j][1] - intervals[j][0]):
                        intervals.insert(i, intervals.pop(j))
                    else:
                        intervals.insert((i + 1), intervals.pop(j))
                elif intervals[i][0] > intervals[j][0]:
                    intervals.insert(i, intervals.pop(j))
        count = left = 0
        right = 1
        while right < len(intervals):
            if intervals[left][1] <= intervals[right][0]:
                left = right
                right += 1
            elif intervals[left][1] <= intervals[right][1]:
                count += 1
                right += 1
            elif intervals[right][0] >= intervals[left][0]:
                count += 1
                left = right
                right += 1
            else:
                right += 1
        return count
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            j = i + 1
            while j < len(intervals):
                if intervals[i][0] == intervals[j][0]:
                    if (intervals[i][1] - intervals[i][0]) < (intervals[j][1] - intervals[j][0]):
                        intervals.insert(i, intervals.pop(j))
                    elif (intervals[i][1] - intervals[i][0]) == (intervals[j][1] - intervals[j][0]):
                        del intervals[j]
                        j -= 1
                    else:
                        intervals.insert((i + 1), intervals.pop(j))
                elif intervals[i][0] > intervals[j][0]:
                    intervals.insert(i, intervals.pop(j))
                j += 1
        left = 0
        right = 1
        while right < len(intervals):
            if intervals[left][1] < intervals[right][0]:
                left = right
                right += 1
            elif intervals[left][1] <= intervals[right][1]:
                if intervals[left][1] == intervals[right][1]:
                    del intervals[right]
                else:
                    intervals[left][1] = intervals.pop(right)[1]
            elif intervals[left][0] <= intervals[right][0]:
                del intervals[right]
            else:
                right += 1
        return intervals
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
```