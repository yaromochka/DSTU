import sys

class Node:
    """ Узел AVL-дерева """
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    """ AVL-дерево с операциями вставки и поиска минимального элемента >= x """
    def __init__(self):
        self.root = None

    def height(self, node):
        """ Возвращает высоту узла """
        return node.height if node else 0

    def balance_factor(self, node):
        """ Вычисляет баланс-фактор узла """
        return self.height(node.left) - self.height(node.right) if node else 0

    def fix_height(self, node):
        """ Обновляет высоту узла """
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, p):
        """ Малое правое вращение """
        q = p.left
        p.left = q.right
        q.right = p
        self.fix_height(p)
        self.fix_height(q)
        return q

    def rotate_left(self, q):
        """ Малое левое вращение """
        p = q.right
        q.right = p.left
        p.left = q
        self.fix_height(q)
        self.fix_height(p)
        return p

    def balance(self, node):
        """ Балансировка узла """
        self.fix_height(node)
        if self.balance_factor(node) == 2:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if self.balance_factor(node) == -2:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, node, key):
        """ Вставка элемента в AVL-дерево """
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return self.balance(node)

    def find_min(self, node, x):
        """ Ищем минимальный элемент >= x """
        if not node:
            return None
        if node.key >= x:
            left_res = self.find_min(node.left, x)
            return left_res if left_res is not None else node.key
        return self.find_min(node.right, x)

    def add(self, key):
        """ Внешний метод для добавления элемента """
        self.root = self.insert(self.root, key)

    def next(self, x):
        """ Внешний метод для поиска min(≥ x) """
        res = self.find_min(self.root, x)
        return res if res is not None else -1

class SortedSet:
    """ Реализация `SortedSet` на основе AVL-дерева """
    def __init__(self):
        self.tree = AVLTree()
        self.last_query = -1  # Последний ответ на "?"

    def add(self, x):
        """ Добавляет x в множество """
        if self.last_query != -1:
            x = (x + self.last_query) % (10**9)
        self.tree.add(x)
        self.last_query = -1  # Сбрасываем

    def next(self, x):
        """ Ищет минимальный элемент >= x """
        self.last_query = self.tree.next(x)
        return self.last_query


def main():
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    sorted_set = SortedSet()
    result = []

    for line in data[1:n + 1]:
        op, x = line.split()
        x = int(x)

        if op == '+':
            sorted_set.add(x)
        else:  # op == '?'
            result.append(str(sorted_set.next(x)))

    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
