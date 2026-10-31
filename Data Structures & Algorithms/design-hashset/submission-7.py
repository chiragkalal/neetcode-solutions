class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def get_hash(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        index = self.get_hash(key)
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = self.get_hash(key)
        cur_list = self.buckets[index]
        # print("cur_list...", cur_list)
        for val_index in range(len(cur_list)):
            if cur_list[val_index] == key:
                cur_list[val_index], cur_list[-1] = cur_list[-1], cur_list[val_index]
                cur_list.pop()
                return
        

    def contains(self, key: int) -> bool:
        index = self.get_hash(key)
        # print(self.buckets[index])
        return key in self.buckets[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)