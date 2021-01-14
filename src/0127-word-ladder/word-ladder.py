# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:
#
#
# 	The first word in the sequence is beginWord.
# 	The last word in the sequence is endWord.
# 	Only one letter is different between each adjacent pair of words in the sequence.
# 	Every word in the sequence is in wordList.
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#  
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog" with 5 words.
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no possible transformation.
#
#
#  
# Constraints:
#
#
# 	1 <= beginWord.length <= 100
# 	endWord.length == beginWord.length
# 	1 <= wordList.length <= 5000
# 	wordList[i].length == beginWord.length
# 	beginWord, endWord, and wordList[i] consist of lowercase English letters.
# 	beginWord != endWord
# 	All the strings in wordList are unique.
#
#


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        
        charSet = set(char for word in wordList for char in word)
        wordList = set(wordList)
        q = deque([(beginWord, 1),])
        
        while q:
            word, step = q.popleft()
            for i in range(len(word)):
                for c in charSet:
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordList:
                        if nextWord == endWord: return step + 1
                        wordList.remove(nextWord)
                        q.append((nextWord, step + 1))
        
        return 0
    
