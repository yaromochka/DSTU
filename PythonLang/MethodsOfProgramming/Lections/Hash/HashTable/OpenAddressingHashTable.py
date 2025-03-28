# Реализация хеш-таблицы с открытой адресацией
class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def _hash(self, key, attempt=0):
        return (hash(key) + attempt) % self.size

    def insert(self, key, value):
        for attempt in range(self.size):
            hash_key = self._hash(key, attempt)
            if self.table[hash_key] is None or self.table[hash_key] is self.deleted:
                self.table[hash_key] = (key, value)
                return
            elif self.table[hash_key][0] == key:
                self.table[hash_key] = (key, value)
                return
        raise Exception("Хеш-таблица переполнена")

    def get(self, key):
        for attempt in range(self.size):
            hash_key = self._hash(key, attempt)
            if self.table[hash_key] is None:
                break
            elif self.table[hash_key] is not self.deleted and self.table[hash_key][0] == key:
                return self.table[hash_key][1]
        raise KeyError(key)

    def delete(self, key):
        for attempt in range(self.size):
            hash_key = self._hash(key, attempt)
            if self.table[hash_key] is None:
                break
            elif self.table[hash_key] is not self.deleted and self.table[hash_key][0] == key:
                self.table[hash_key] = self.deleted
                return
        raise KeyError(key)

    def __str__(self):
        return str(self.table)