# Реализация изменяемой хеш-таблицы с методом цепочек
from PythonLang.MethodsOfProgramming.Lections.Hash.HashTable.HashTable import HashTable


class ResizableHashTable(HashTable):
    def __init__(self, initial_size=10, load_factor=0.7):
        super().__init__(initial_size)
        self.load_factor = load_factor
        self.count = 0

    def insert(self, key, value):
        if self.count / self.size > self.load_factor:
            self._resize()
        super().insert(key, value)
        self.count += 1

    def _resize(self):
        new_size = self.size * 2
        new_table = [[] for _ in range(new_size)]

        old_table = self.table
        self.table = new_table
        self.size = new_size
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)