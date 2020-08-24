# Implement the StreamChecker class as follows:
#
#
# 	StreamChecker(words): Constructor, init the data structure with the given words.
# 	query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
#
#
#  
#
# Example:
#
#
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the wordlist
#
#
#  
#
# Note:
#
#
# 	1 <= words.length <= 2000
# 	1 <= words[i].length <= 2000
# 	Words will only consist of lowercase English letters.
# 	Queries will only consist of lowercase English letters.
# 	The number of queries is at most 40000.
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


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words: self.trie.insert(w[::-1])
        self.stream = deque()

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        cur = self.trie.root
        for c in self.stream:
            if c in cur.children:
                cur = cur.children[c]
                if cur.end_node: return True
            else: break
        return False
    

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
