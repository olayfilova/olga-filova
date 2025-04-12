class CustomHashMap:
    def __init__(self, initial_capacity=8, load_factor=0.7):
        self.capacity = initial_capacity  # Розмір хеш-таблиці
        self.size = 0  # Кількість збережених елементів
        self.load_factor = load_factor  # Межа заповненості
        self.table = [None] * self.capacity  # Створюємо пусту таблицю


    def _hash(self, key):
        return hash(key) % self.capacity


    def _insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            k, _ = self.table[index]
            if k == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.capacity  # перехід до наступної комірки
        self.table[index] = (key, value)
        self.size += 1


    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for entry in old_table:
            if entry is not None:
                self._insert(entry[0], entry[1])


    def set(self, key, value):
        self._insert(key, value)


    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                return v
            index = (index + 1) % self.capacity
        raise KeyError(f"Key '{key}' not found.")

    def __setitem__(self, key, value):
        self.set(key, value)


    def __getitem__(self, key):
        return self.get(key)


    def __str__(self):
        return "{" + ", ".join(
            f"{k}: {v}" for k, v in self.table if k is not None
        ) + "}"


hash_map = CustomHashMap()
hash_map._insert("name", "John")
print(hash_map.get("name"))  # виведе "John"
print(hash("name"))


#rehash
# hash_map = CustomHashMap(initial_capacity=8, load_factor=0.7)
#
# # Вставляємо 9 ключів
# hash_map._insert("key1", "value1")
# hash_map._insert("key2", "value2")
# hash_map._insert("key3", "value3")
# hash_map._insert("key4", "value4")
# hash_map._insert("key5", "value5")
# hash_map._insert("key6", "value6")
# hash_map._insert("key7", "value7")
# hash_map._insert("key8", "value8")
# hash_map._insert("key9", "value9")
#
# # Перевіряємо значення
# for i in range(1, 10):
#     print(hash_map.get(f"key{i}"))

