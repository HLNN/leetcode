# Design and implement a data structure for a Least Frequently Used (LFU) cache.
#
# Implement the LFUCache class:
#
#
# 	LFUCache(int capacity) Initializes the object with the capacity of the data structure.
# 	int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
# 	void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
#
#
# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.
#
# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.
#
# The functions get and put must each run in O(1) average time complexity.
#
#  
# Example 1:
#
#
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#
#
#  
# Constraints:
#
#
# 	0 <= capacity <= 104
# 	0 <= key <= 105
# 	0 <= value <= 109
# 	At most 2 * 105 calls will be made to get and put.
#
#
#  
#  


class LFUCache:
    def __init__(self, capacity: int):
        self.minFreq = 0
        self.cap = capacity
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freqToKeys = defaultdict(LinkedHashSet)

    def p(self):
        print('minf:\t', self.minFreq)
        print('kv:\t', self.keyToVal)
        print('kf:\t', self.keyToFreq)
        for k, v in self.freqToKeys.items():
            print(k, v)
        print()

    def get(self, key):
        if key not in self.keyToVal:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def put(self, key, value):
        if self.cap <= 0: return

        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.increaseFreq(key)
        else:
            if self.cap <= len(self.keyToVal):
                self.removeMinFreq()
            self.addNew(key, value)

    def increaseFreq(self, key):
        freq = self.keyToFreq[key]
        self.keyToFreq[key] += 1

        node = self.freqToKeys[freq].remove(key)
        self.freqToKeys[freq + 1].add(key, node)

        if len(self.freqToKeys[freq]) == 0 and freq == self.minFreq:
            self.minFreq += 1

    def removeMinFreq(self):
        node = self.freqToKeys[self.minFreq].removeFirst()
        if node:
            del self.keyToVal[node.key]
            del self.keyToFreq[node.key]

    def addNew(self, key, value):
        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        self.freqToKeys[1].add(key)
        self.minFreq = 1


class LinkedHashSet:
    def __init__(self):
        self.doubleList = DoubleList()
        self.map = {}
    
    def __len__(self):
        return len(self.doubleList)
    
    def __str__(self):
        return str(self.doubleList)
    
    def add(self, key, node=None):
        if not node:
            node = Node(key)
        self.map[key] = node
        self.doubleList.addLast(node)
    
    def remove(self, key):
        node = self.map[key]
        self.doubleList.removeAt(node)
        del self.map[key]
        return node
    
    def removeFirst(self):
        node = self.doubleList.removeFirst()
        if node:
            del self.map[node.key]
        return node


class DoubleList:
    def __init__(self):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        res = []
        head = self.head.next
        while head != self.tail:
            res.append(head.key)
            head = head.next
        return str(res)

    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1

    def removeAt(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        x = self.head.next
        self.removeAt(x)
        return x


class Node:
    def __init__(self, k, v=0):
        self.key = k
        self.value = v
        self.prev, self.next = None, None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
