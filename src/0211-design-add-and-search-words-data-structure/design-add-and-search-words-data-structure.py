# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# 	WordDictionary() Initializes the object.
# 	void addWord(word) Adds word to the data structure, it can be matched later.
# 	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
#  
# Example:
#
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#  
# Constraints:
#
#
# 	1 <= word.length <= 25
# 	word in addWord consists of lowercase English letters.
# 	word in search consist of '.' or lowercase English letters.
# 	There will be at most 3 dots in word for search queries.
# 	At most 104 calls will be made to addWord and search.
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
