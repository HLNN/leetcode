# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
#  
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n = board[i].length
# 	1 <= m, n <= 6
# 	1 <= word.length <= 15
# 	board and word consists of only lowercase and uppercase English letters.
#
#
#  
# Follow up: Could you use search pruning to make your solution faster with a larger board?
#


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if len(word) > m * n: return False
        if not (cnt := Counter(word)) <= Counter(chain(*board)): return False
        
        if cnt[word[0]] > cnt[word[-1]]:
            word = word[::-1]
        
        d = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        def dfs(x, y, i, ch='#'):
            if i == len(word): return True
            
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[i]:
                board[x][y], ch = ch, board[x][y]
                dp = any(dfs(x + dx, y + dy, i + 1) for dx, dy in d)
                board[x][y], ch = ch, board[x][y]
                return dp
            
            return False
        
        return any(dfs(x, y, 0) for x, y in product(range(m), range(n)))
    
