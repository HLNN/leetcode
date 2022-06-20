# You are given an array of strings products and a string searchWord.
#
# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.
#
# Return a list of lists of the suggested products after each character of searchWord is typed.
#
#  
# Example 1:
#
#
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
#
#
# Example 2:
#
#
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
#
#
# Example 3:
#
#
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
# Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
#
#
#  
# Constraints:
#
#
# 	1 <= products.length <= 1000
# 	1 <= products[i].length <= 3000
# 	1 <= sum(products[i].length) <= 2 * 104
# 	All the strings of products are unique.
# 	products[i] consists of lowercase English letters.
# 	1 <= searchWord.length <= 1000
# 	searchWord consists of lowercase English letters.
#
#


class Trie:
    def __init__(self, w='', i=0):
        self.ans = []
        self.children = {}
        self.insert(w, i)
        
    def insert(self, w, i=0):
        if len(self.ans) < 3: self.ans.append(w)
            
        if i < len(w):
            if w[i] in self.children:
                self.children[w[i]].insert(w, i + 1)
            else:
                self.children[w[i]] = Trie(w, i + 1)
    
    def search(self, w, i=0):
        if i == len(w):
            return self.ans
        elif w[i] not in self.children:
            return []
        else:
            return self.children[w[i]].search(w, i + 1)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(list(set(products)))
        
        trie = Trie()
        for w in products:
            trie.insert(w)
        
        return [trie.search(searchWord[:i]) for i in range(1, len(searchWord) + 1)]
    
