# You are given an m x n grid grid where:
#
#
# 	'.' is an empty cell.
# 	'#' is a wall.
# 	'@' is the starting point.
# 	Lowercase letters represent keys.
# 	Uppercase letters represent locks.
#
#
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.
#
# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
#
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
#
# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
#
#  
# Example 1:
#
#
# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.
#
#
# Example 2:
#
#
# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
#
#
# Example 3:
#
#
# Input: grid = ["@Aa"]
# Output: -1
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 30
# 	grid[i][j] is either an English letter, '.', '#', or '@'.
# 	The number of keys in the grid is in the range [1, 6].
# 	Each key in the grid is unique.
# 	Each key in the grid has a matching lock.
#
#


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        low = 'abcdef' # key
        up = 'ABCDEF' # lock
        m, n = len(grid), len(grid[0])
        keys = sum(c in low for c in set(chain.from_iterable(grid)))

        for i, j in product(range(m), range(n)):
            if grid[i][j] == '@':
                start = (i, j, '*' * keys)
        seen = set([start])
        q = deque([(start, 1)])
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))

        while q:
            (x, y, locks), res = q.popleft()
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                locks_new = locks
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#':
                    if grid[nx][ny] in low:
                        # add key
                        idx = ord(grid[nx][ny]) - 97
                        if locks[idx] == '*':
                            locks_new = locks[:idx] + '-' + locks[idx + 1:]
                    elif grid[nx][ny] in up:
                        # check key
                        idx = ord(grid[nx][ny]) - 65
                        if locks[idx] == '*': continue
                        elif locks[idx] == '-':
                            # unlock
                            locks_new = locks[:idx] + '+' + locks[idx + 1:]
                    if all(l != '*' for l in locks_new): return res
                    
                    status = (nx, ny, locks_new)
                    if status not in seen:
                        seen.add(status)
                        q.append((status, res + 1))
            # print(q)
        
        return -1
    
