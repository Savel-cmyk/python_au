# Dynamic-programming

+ [House Robber II](#house-robber-ii)
+ [House Robber](#house-robber)

## House Robber II

https://leetcode.com/problems/house-robber-ii/

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        dp1, dp2 = 0, 0
        for n in nums[:-1]:
            tmp = dp1
            dp1 = max(dp2 + n, dp1)
            dp2 = tmp
            
        dpp1, dpp2 = 0, 0
        for n in nums[1:]:
            tmp = dpp1
            dpp1 = max(dpp2 + n, dpp1)
            dpp2 = tmp
            
        return max(dp1, dpp1)
```

## House Robber

https://leetcode.com/problems/house-robber/

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        dp1, dp2 = 0, 0
        for n in nums:
            tmp = dp1
            dp1 = max(dp2 + n, dp1)
            dp2 = tmp
            
        return dp1
```