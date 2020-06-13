# Design a data structure that supports all following operations in average O(1) time.
#
#
#
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
#
#
#
# Example:
#
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
#
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
#
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
#
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
#
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
#
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
#
# // 2 was already in the set, so return false.
# randomSet.insert(2);
#
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();
#
#


class RandomizedSet:
    def __init__(self):
        self.dic_direct = {}
        self.dic_invert = {}
        self.num_elem = 0
        
    def insert(self, val: int) -> bool:
        if val in self.dic_invert:
            return False
        else:
            self.dic_invert[val] = self.num_elem
            self.dic_direct[self.num_elem] = val
            self.num_elem += 1
            return True
        
    def remove(self, val):
        if val not in self.dic_invert:
            return False
        else:
            ind = self.dic_invert.pop(val)
            self.dic_direct.pop(ind)
            if ind != self.num_elem - 1:
                self.dic_direct[ind] = self.dic_direct[self.num_elem - 1]
                self.dic_invert[self.dic_direct[self.num_elem - 1]] = ind
                self.dic_direct.pop(self.num_elem - 1)
            self.num_elem -= 1
            return True
        
    def getRandom(self):
        index = floor(random.random()*self.num_elem)
        return self.dic_direct[index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
