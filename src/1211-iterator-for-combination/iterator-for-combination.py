# Design the CombinationIterator class:
#
#
# 	CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# 	next() Returns the next combination of length combinationLength in lexicographical order.
# 	hasNext() Returns true if and only if there exists a next combination.
#
#
#  
# Example 1:
#
#
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]
#
# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False
#
#
#  
# Constraints:
#
#
# 	1 <= combinationLength <= characters.length <= 15
# 	All the characters of characters are unique.
# 	At most 104 calls will be made to next and hasNext.
# 	It is guaranteed that all calls of the function next are valid.
#
#


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.charactersLength = len(characters)
        self.combinationLength = combinationLength
        self.comb = self._combination(self.combinationLength)
        self.i = 0
        self.resLength = len(self.comb)
    
    def _combination(self, n):
        def bt(pos, num, ans):
            if num == self.combinationLength:
                res.append(ans)
            elif pos == self.charactersLength or self.charactersLength - pos + 1 + num < self.combinationLength:
                # no pos to put 1
                return
            else:
                bt(pos + 1, num + 1, ans | 1 << pos)
                bt(pos + 1, num, ans)
                
        res = []
        bt(0, 0, 0)
        return res

    def next(self) -> str:
        n = self.comb[self.i]
        self.i += 1
        return ''.join([self.characters[x] for x in range(self.charactersLength) if n & 1 << x])

    def hasNext(self) -> bool:
        return self.i < self.resLength


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
