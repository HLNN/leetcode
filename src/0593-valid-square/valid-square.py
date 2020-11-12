# Given the coordinates of four points in 2D space, return whether the four points could construct a square.
#
# The coordinate (x,y) of a point is represented by an integer array with two integers.
#
# Example:
#
#
# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True
#
#
#  
#
# Note:
#
#
# 	All the input integers are in the range [-10000, 10000].
# 	A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# 	Input points have no order.
#
#
#  
#


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        @lru_cache()
        def dist(p1, p2):
            return (self.p[p2-1][1] - self.p[p1-1][1]) ** 2 + (self.p[p2-1][0] - self.p[p1-1][0]) ** 2
        
        def check(p1, p2, p3, p4):
            return dist(p1, p2) > 0 and dist(p1, p2) == dist(p2, p3) and dist(p2, p3) == dist(p3, p4) and dist(p3, p4) == dist(p4, p1) and dist(p1, p3) == dist(p2, p4)
        
        self.p = (p1, p2, p3, p4)
        return check(1, 2, 3, 4) or check(1, 3, 2, 4) or check(1, 2, 4, 3)
    
