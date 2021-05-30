# Graph

+ [Course Schedule II](#course-schedule-ii)
+ [Course Schedule](#course-schedule)
+ [Number of Islands](#number-of-islands)
+ [Is Graph Bipartite?](#is-graph-bipartite)
+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)
+ [Shortest Path in Binary Matrix](#shortest-path-in-binary-matrix)
+ [Maximum Depth of N-ary Tree](#maximum-depth-of-n-ary-tree)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            output.append(crs)
            visit.add(crs)
            return True

        for num in range(numCourses):
            if dfs(num) == False:
                return []
        return output
```

## Course Schedule

https://leetcode.com/problems/course-schedule/

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = { c:[] for c in range(numCourses) }
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        for num in range(numCourses):
            if dfs(num) == False:
                return False
        return True
```

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands
```

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        col = [-1]*N
        
        for i in range(N):
            if col[i] != -1:
                continue
            q = collections.deque()
            q.append((i, 0))
            while q:
                node, color = q.popleft()
                if col[node] == -1:
                    col[node] = color
                    for nx in graph[node]:
                        q.append((nx, color^1))
                if col[node] != color:
                    return False
        return True
```

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        output = [float('inf') for _ in range(n)]
        output[src] = 0

        for u, v, w in flights:
            adj[u].append((v, w))

        graph = deque()
        graph.append((src, -1, 0))

        while graph:
            u, stop, cost = graph.popleft()
            if stop >= k:
                continue
            for v, w in adj[u]:
                if (cost + w) < output[v]:
                    output[v] = cost + w
                    graph.append((v, stop + 1, cost + w))

        if output[dst] == float('inf'):
            return -1
        else:
            return output[dst]
```

## Shortest Path in Binary Matrix

https://leetcode.com/problems/shortest-path-in-binary-matrix/

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        if grid[0][0] == 0:
            q.append((1, (0, 0)))
            grid[0][0] = 1

        while q:
            steps, tmp = q.popleft()
            r, c = tmp[0], tmp[1]
            if (r, c) == (M - 1, N - 1):
                return steps
            for i, j in dirs:
                new_r, new_c = r + i, c + j
                if (0 <= new_r < M and
                    0 <= new_c < N and
                    grid[new_r][new_c] == 0 and
                    (new_r, new_c) not in visited):
                    q.append((steps + 1, (new_r, new_c)))
                    grid[new_r][new_c] = 1
        return -1
```

## Maximum Depth of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        a=[]
        if not root:
            return 0
        if len(root.children) == 0:
            return 1
        for c in root.children:
            a.append(self.maxDepth(c))
        return max(a)+1
```