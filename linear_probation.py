class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key already exists, update the value
                self.values[index] = value
                return
            # Linear probing to find the next available slot
            index = (index + 1) % self.size

        # Found an empty slot, insert the key and value
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            # Linear probing to search for the key
            index = (index + 1) % self.size

        # Key not found
        return None

# Create a hash table with a size of 5
hash_table = HashTable(5)

# Insert key-value pairs
hash_table.put("apple", 5)
hash_table.put("banana", 2)
hash_table.put("cherry", 8)

# Retrieve values
print(hash_table.get("apple"))  # Output: 5
print(hash_table.get("banana"))  # Output: 2
print(hash_table.get("cherry"))  # Output: 8
print(hash_table.get("grape"))   # Output: None (key not found)