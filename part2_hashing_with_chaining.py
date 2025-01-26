class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        # Universal hash function: h(k) = (a * k + b) % p % m
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key exists; update if it does
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Add a new key-value pair
        self.table[index].append([key, value])
        self.num_elements += 1
        # Resize if load factor exceeds 0.75
        if self.num_elements / self.size > 0.75:
            self._resize()

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                self.num_elements -= 1
                return True
        return False  # Key not found

    def _resize(self):
        # Double the size and rehash all elements
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]
        for chain in self.table:
            for key, value in chain:
                new_index = hash(key) % new_size
                new_table[new_index].append([key, value])
        self.size = new_size
        self.table = new_table

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

if __name__ == "__main__":
    # Example usage
    ht = HashTable()
    ht.insert("key1", "value1")
    ht.insert("key2", "value2")
    ht.insert("key3", "value3")
    ht.insert("key1", "updated_value1")  # Update existing key

    print(ht.search("key1"))  # Output: updated_value1
    print(ht.search("key4"))  # Output: None

    ht.delete("key2")
    print(ht.search("key2"))  # Output: None

    ht.display()  # Print the hash table contents