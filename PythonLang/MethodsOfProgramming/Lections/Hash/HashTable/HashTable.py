class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Создаем список списков

    def _hash(self, key):
        # Простая хеш-функция: сумма ASCII-кодов символов ключа по модулю size
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        bucket.append((key, value))
        return

    def get(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(key)

    def __str__(self):
        return str(self.table)