# You are given a 2D array of axis-aligned rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] denotes the ith rectangle where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner.
#
# Calculate the total area covered by all rectangles in the plane. Any area covered by two or more rectangles should only be counted once.
#
# Return the total area. Since the answer may be too large, return it modulo 109 + 7.
#
#  
# Example 1:
#
#
# Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: A total area of 6 is covered by all three rectangales, as illustrated in the picture.
# From (1,1) to (2,2), the green and red rectangles overlap.
# From (1,0) to (2,3), all three rectangles overlap.
#
#
# Example 2:
#
#
# Input: rectangles = [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 1018 modulo (109 + 7), which is 49.
#
#
#  
# Constraints:
#
#
# 	1 <= rectangles.length <= 200
# 	rectanges[i].length == 4
# 	0 <= xi1, yi1, xi2, yi2 <= 109
#
#


class Node:
    def __init__(self, start: int, end: int, X: List[int]) -> None:
        self.start, self.end = start, end
        self.total = self.count = 0
        self._left = self._right = None
        self.X = X

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        self._left = self._left or Node(self.start, self.mid, self.X)
        return self._left

    @property
    def right(self):
        self._right = self._right or Node(self.mid, self.end, self.X)
        return self._right

    def update(self, i: int, j: int, val: int) -> int:
        if i >= j: return 0
        if self.start == i and self.end == j:
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val)
            self.right.update(max(self.mid, i), j, val)

        if self.count > 0:
            self.total = self.X[self.end] - self.X[self.start]
        else:
            self.total = self.left.total + self.right.total

        return self.total

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        events = []
        
        X = set()
        for x1, y1, x2, y2 in rectangles:
            if (x1 < x2) and (y1 < y2):
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
                X.add(x1)
                X.add(x2)
        events.sort()

        X = sorted(X)
        x_index = {x: i for i, x in enumerate(X)}
        active = Node(0, len(X) - 1, X)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            cur_x_sum = active.update(x_index[x1], x_index[x2], typ)
            cur_y = y

        return ans % (10**9 + 7)
    
