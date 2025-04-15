# Примеры хеш-функций
from PythonLang.MethodsOfProgramming.Lections.Hash.HashTable.HashTable import HashTable
from PythonLang.MethodsOfProgramming.Lections.Hash.HashTable.OpenAddressingHashTable import OpenAddressingHashTable
from PythonLang.MethodsOfProgramming.Lections.Hash.HashTable.ResizableHashTable import ResizableHashTable


def simple_hash(key, table_size):
    return sum(ord(c) for c in str(key)) % table_size


def djb2_hash(key, table_size):
    hash_value = 5381
    for c in str(key):
        hash_value = (hash_value * 33) + ord(c)
    return hash_value % table_size


def multiplicative_hash(key, table_size):
    A = 2654435769
    return (key * A) % (2 ** 32) % table_size


# Примеры использования
if __name__ == "__main__":
    print("### HashTable с цепочками ###")
    ht = HashTable()
    ht.insert("apple", 10)
    ht.insert("orange", 20)
    ht.insert("egnaro", 20)
    ht.insert("orange", 150)
    ht.insert("banana", 27)
    ht.insert("banana", 30)
    ht.insert("apple", 15)
    print(ht)
    print(ht.get("orange"))
    ht.delete("orange")

    print("\n### OpenAddressingHashTable ###")
    oht = OpenAddressingHashTable()
    oht.insert(1, "one")
    oht.insert(11, "eleven")
    oht.insert(11, "two")
    oht.insert(21, "twenty-one")
    print(oht.get(1))
    print(oht.get(11))
    print(oht)
    oht.delete(11)

    print("\n### ResizableHashTable ###")
    rht = ResizableHashTable(5, 0.6)
    for i in range(10):
        rht.insert(f"key{i}", i)
        print(f"Inserted key{i}, size: {rht.size}, count: {rht.count}")
    print(rht)
