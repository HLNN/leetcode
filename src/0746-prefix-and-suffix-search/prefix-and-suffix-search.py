# Design a special dictionary that searches the words in it by a prefix and a suffix.
#
# Implement the WordFilter class:
#
#
# 	WordFilter(string[] words) Initializes the object with the words in the dictionary.
# 	f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
#
#
#  
# Example 1:
#
#
# Input
# ["WordFilter", "f"]
# [[["apple"]], ["a", "e"]]
# Output
# [null, 0]
# Explanation
# WordFilter wordFilter = new WordFilter(["apple"]);
# wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
#
#
#  
# Constraints:
#
#
# 	1 <= words.length <= 104
# 	1 <= words[i].length <= 7
# 	1 <= pref.length, suff.length <= 7
# 	words[i], pref and suff consist of lowercase English letters only.
# 	At most 104 calls will be made to the function f.
#
#


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie={}
        self.weight_marker='$'
        w=self.weight_marker
        for idx, word in enumerate(words):
            word=word + '#'
            length=len(word)
            word+=word
            
            for i in range(length):
                curr=self.trie
                curr[w]=idx 
                for c in word[i:]:
                    if c not in curr:
                        curr[c]={}
                    curr=curr[c]                    
                    curr[w]=idx  # update the weight of substring                        
            

    def f(self, prefix: str, suffix: str) -> int:
        curr=self.trie
        for c in suffix + '#' + prefix:
            if c not in curr:
                return -1
            curr=curr[c]
        
        return curr[self.weight_marker]


# MY SULUTION -- Time Limit Exceeded
# class Trie:
#     def __init__(self, w='', i=-1):
#         self.children = {}
#         self.idx = i
#         self.insert(w, i)
    
#     def insert(self, w, i):
#         self.idx = i
#         if w:
#             if w[0] in self.children:
#                 self.children[w[0]].insert(w[1:], i)
#             else:
#                 self.children[w[0]] = Trie(w[1:], i)
    
#     def search(self, w, i=0):
#         if i == len(w):
#             return self.idx
#         elif w[i] not in self.children:
#             return -1
#         else:
#             return self.children[w[i]].search(w, i + 1)


# class WordFilter:
#     def __init__(self, words):
#         self.trie = Trie()
#         self.words = {w: idx for idx, w in enumerate(words)}
        
#         for w, idx in self.words.items():
#             n, ww = len(w), '&'.join((w, w))
#             for i in range(n + 1):
#                 self.trie.insert(ww[i:], idx)

#     def f(self, prefix: str, suffix: str) -> int:
#         return self.trie.search('&'.join((suffix, prefix)))


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
