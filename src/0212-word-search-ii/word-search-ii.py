# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#  
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 12
# 	board[i][j] is a lowercase English letter.
# 	1 <= words.length <= 3 * 104
# 	1 <= words[i].length <= 10
# 	words[i] consists of lowercase English letters.
# 	All the strings of words are unique.
#
#


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for symbol in word:
            dic_to_search = root.children
            if symbol not in dic_to_search: 
                dic_to_search[symbol] = TrieNode()
            root.children = dic_to_search
            root = root.children[symbol]
        root.end_node = True

        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.num_words = len(words)
        res, trie = [], Trie()
        for word in words: trie.insert(word)
            
        for i, j in product(range(len(board)), range(len(board[0]))):
            self.dfs(board, trie.root, i, j, "", res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if self.num_words == 0: return
    
        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return
        tmp = board[i][j]
        if tmp not in node.children: return 
        
        board[i][j] = "#"
        for x, y in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        board[i][j] = tmp
        
