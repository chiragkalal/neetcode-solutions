class MyHashMap:
    # put -> {1: 1, 2: 2} 
    # get -> 1 -> 1, 3 -> -1,
    # put -> updated {2: 1} -> get 2 -> 1 -> remove 2 -> {1: 1} -> get 2 -> -1
    """Implment with list and tuple
        tuple -> (key, value)
        list chaining method -> [[(k1, v1), (k2, v2)], [], [], []]
    """

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for i in range(self.size)]
    
    def get_hash(self, key):
        return hash(key) % self.size

    def put(self, key: int, value: int) -> None:
        index = self.get_hash(key)
        items = self.buckets[index]
        for item_index in range(len(items)):
            k, v = items[item_index]
            if k == key:
                items[item_index] = (key, value)
                # print(f"Insert -> ({key}, {value})")
                return
        items.append((key, value))
        # print(f"Insert -> ({key}, {value})")

    def get(self, key: int) -> int:
        index = self.get_hash(key)
        items = self.buckets[index]
        for item_index in range(len(items)):
            k, v = items[item_index]
            if k == key:
                # print(f"Found value of {key} -> {v}")
                return v
        # print(f"Found value of {key} -> -1")
        return -1
        

    def remove(self, key: int) -> None:
        index = self.get_hash(key)
        items = self.buckets[index]
        for item_index in range(len(items)):
            k, v = items[item_index]
            if k == key:
                items[item_index], items[-1] = items[-1], items[item_index]
                removed_item = items.pop()
                # print(f"removed item -> {removed_item}")
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)