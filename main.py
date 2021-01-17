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