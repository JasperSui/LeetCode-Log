class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.item_list = []
        self.item_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.item_index: return False
        else:
            self.item_list.append(val)
            self.item_index[val] = len(self.item_list) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.item_index:
            index = self.item_index[val]
            last = self.item_list[-1]
            self.item_list[index] = last
            self.item_index[last] = index
            self.item_list.pop()
            del self.item_index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.item_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()