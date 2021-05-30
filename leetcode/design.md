# Design

+ [Min Stack](#min-stack)
+ [Implement Queue using Stacks](#implement-queue-using-stacks)
+ [Implement Stack using Queues](#implement-stack-using-queues)
+ [Design Twitter](#design-twitter)

## Min Stack

https://leetcode.com/problems/min-stack/

```python
class MinStack:
    def __init__(self, opt=[]):
        self.stack = list(opt)
        
    def push(self, val: int) -> None:
        self.stack.append(val)
    
    def pop(self) -> None:
        if len(self.stack): self.stack.pop()

    def top(self) -> int:
        if len(self.stack): return self.stack[len(self.stack) - 1]
    
    def getMin(self) -> int:
        min = self.stack[len(self.stack)-1]        
        for i in range(len(self.stack)-1):
            if min > self.stack[i]:
                min = self.stack[i]
        return min
```

## Implement Queue using Stacks

https://leetcode.com/problems/implement-queue-using-stacks/

```python
class MyQueue:
    def __init__(self, opt = []):
        self.stack = collections.deque(opt)

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack): return self.stack.popleft()

    def peek(self) -> int:
        if len(self.stack): return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
```

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
class MyStack:
    def __init__(self, opt = []):
        self.stack = list(opt)

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack): return self.stack.pop()

    def top(self) -> int:
        if len(self.stack): return self.stack[len(self.stack) - 1]

    def empty(self) -> bool:
        return len(self.stack) == 0
```

## Design Twitter

https://leetcode.com/problems/design-twitter/

```python
class Twitter:
    def __init__(self):
        self.__number_of_most_recent_tweets = 10
        self.__followings = collections.defaultdict(set)
        self.__messages = collections.defaultdict(list)
        self.__time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.__time += 1
        self.__messages[userId].append((self.__time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        if self.__messages[userId]:
            heapq.heappush(max_heap, (-self.__messages[userId][-1][0], userId, 0))
        for uid in self.__followings[userId]:
            if self.__messages[uid]:
                heapq.heappush(max_heap, (-self.__messages[uid][-1][0], uid, 0))
                
        result = []
        while max_heap and len(result) < self.__number_of_most_recent_tweets:
            t, uid, curr = heapq.heappop(max_heap)
            nxt = curr + 1
            if nxt < len(self.__messages[uid]):
                heapq.heappush(max_heap, (-self.__messages[uid][~nxt][0], uid, nxt))
            result.append(self.__messages[uid][~curr][1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId: self.__followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.__followings[followerId].discard(followeeId)
```