class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indexes = defaultdict(set)
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        self.indexes[val].add(len(self.nums)-1)
        return len(self.indexes[val]) == 1
            

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.indexes[val]:
            index = self.indexes[val].pop()
            last = self.nums[-1]
            self.nums[index] = last
            self.indexes[last].add(index)
            self.indexes[last].remove(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()