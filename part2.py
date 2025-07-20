import random

class HashTableChaining:
    def __init__(self, size=10, prime=109345121):
        self.size = size                        # number of buckets
        self.table = [[] for _ in range(size)] # list of buckets
        self.p = prime                          # large prime number for hashing
        self.a = random.randint(1, prime - 1)   # random multiplier
        self.b = random.randint(0, prime - 1)   # random increment

    def _hash(self, key):
        """Universal hash function: ((a * key + b) % p) % size"""
        key_hash = hash(key)
        return ((self.a * key_hash + self.b) % self.p) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Update value if key exists
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        # Otherwise insert new
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None  # not found

    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False  # not found

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
            
if __name__ == "__main__":
    ht = HashTableChaining(size=7)

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("orange", 150)

    print("Search apple:", ht.search("apple"))       # Output: 100
    print("Search banana:", ht.search("banana"))     # Output: 200

    ht.delete("banana")
    print("After deleting banana:")
    print("Search banana:", ht.search("banana"))     # Output: None

    ht.display()
