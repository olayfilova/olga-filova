class Hashing:
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size  # Initialize the table with -1 indicating empty slots

    def Hash(self, x):
        return x % self.size

    def Insert(self, x):
        k = self.Hash(x)
        while self.table[k] != -1:  # Check if the slot is occupied
            k = (k + 1) % self.size
        self.table[k] = x

    def Search(self, x):
        k = self.Hash(x)
        while self.table[k] != x:
            if self.table[k] == -1:  # Slot has never been occupied
                return False
            k = (k + 1) % self.size
        return self.table[k] == x

    def Delete(self, x):
        k = self.Hash(x)
        while self.table[k] != x:
            if self.table[k] == -1:  # Slot has never been occupied
                return
            k = (k + 1) % self.size
        if self.table[k] == x:
            self.table[k] = -float('inf')  # Replace with negative infinity to mark the slot as deleted