class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if b>a:
            a, b = b, a
        
        count = 0
        while a>0 or c>0:
            a_, b_, c_ = a%2, b%2, c%2
            if c_ == 0:
                count += a_
                count += b_
            else:
                if not a_ and not b_:
                    count += 1
            a, b, c = a//2, b//2, c//2

        return count