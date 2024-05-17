class HashTable:
  def __init__(self, capacity=4):
    self.capacity = capacity
    self.table = [None] * capacity  # Initialize table with slots for 4 elements

  def _hash(self, key):
    "Simple hash function to calculate an index"
    return sum(ord(char) for char in str(key)) % self.capacity  # Modulo for table size

  def insert(self, key, value):
    "Inserts a key-value pair"
    index = self._hash(key)
    # Directly assign key-value pair to the slot
    self.table[index] = (key, value)

  def get(self, key):
    "Retrieves the value for a key"
    index = self._hash(key)
    # Check if slot has a key-value pair and if the key matches
    if self.table[index] is not None and self.table[index][0] == key:
      return self.table[index][1]  # Return value
    return None  # Key not found

  def remove(self, key):
    "Removes a key-value pair"
    index = self._hash(key)
    # Check if slot has a key-value pair and if the key matches
    if self.table[index] is not None and self.table[index][0] == key:
      # Set the slot to None to indicate removal
      self.table[index] = None
      return True  # Key removed successfully
    return False  # Key not found

  def __str__(self):
    "String representation of the hash table"
    items = []
    for i in range(self.capacity):
      if self.table[i] is not None:
        items.append(f"({self.table[i][0]}, {self.table[i][1]})")
    return "{" + ", ".join(items) + "}"
  

 
  