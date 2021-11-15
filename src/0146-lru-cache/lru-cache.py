# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
#
# 	LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# 	int get(int key) Return the value of the key if the key exists, otherwise return -1.
# 	void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
#
#
# The functions get and put must each run in O(1) average time complexity.
#
#  
# Example 1:
#
#
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
#
#
#  
# Constraints:
#
#
# 	1 <= capacity <= 3000
# 	0 <= key <= 104
# 	0 <= value <= 105
# 	At most 2 * 105 calls will be made to get and put.
#
#


class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.double_link = DoubleLink()
        self.cap = capacity

    def makeRecently(self, key):
        x = self.hash_map[key]
        self.double_link.remove_at(x)
        self.double_link.add_last(x)

    def addRecently(self, key, value):
        x = Node(key, value)
        self.double_link.add_last(x)
        self.hash_map[key] = x
        if self.double_link.size > self.cap:
            self.removeLeastRecently()

    def deleteKey(self, key):
        x = self.hash_map[key]
        self.double_link.remove_at(x)
        del self.hash_map[key]

    def removeLeastRecently(self):
        node = self.double_link.remove_first()
        del self.hash_map[node.key]

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.makeRecently(key)
            return self.hash_map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map[key].value = value
            self.makeRecently(key)
        else:
            self.addRecently(key, value)


class DoubleLink:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def add_last(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def remove_at(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def remove_first(self):
        if self.head.next == self.tail:
            return None
        x = self.head.next
        self.remove_at(x)
        return x


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev, self.next = None, None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

