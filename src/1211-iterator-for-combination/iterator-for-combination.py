# Design an Iterator class, which has:
#
#
# 	A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# 	A function next() that returns the next combination of length combinationLength in lexicographical order.
# 	A function hasNext() that returns True if and only if there exists a next combination.
#
#
#  
#
# Example:
#
#
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
#
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
#
#
#  
# Constraints:
#
#
# 	1 <= combinationLength <= characters.length <= 15
# 	There will be at most 10^4 function calls per test.
# 	It's guaranteed that all calls of the function next are valid.
#
#


from os.path import commonprefix
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.len = combinationLength
        self.state = ""
        
    def next(self) -> str:
        if self.state == "":
            self.state = self.c[:self.len]
        else:
            end = len(commonprefix([self.c[::-1], self.state[::-1]]))
            place = self.c.index(self.state[-end-1])
            self.state = self.state[:-end-1] + self.c[place + 1: place + 2 + end]
        return self.state
        
    def hasNext(self) -> bool:
        return self.state != self.c[-self.len:]

    
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
