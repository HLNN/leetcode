# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
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
        
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, i):
            if i == len(word):
                return node.end_node
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i+1): return True
            elif word[i] in node.children:
                if dfs(node.children[word[i]], i+1): return True
            return False
        return dfs(self.trie.root, 0)
    
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
