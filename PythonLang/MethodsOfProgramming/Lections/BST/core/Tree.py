from PythonLang.MethodsOfProgramming.Lections.BST.core.Node import Node


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # 1. Узел без детей или с одним ребёнком
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 2. Узел с двумя детьми -> находим минимальный в правом поддереве
            min_larger_node = self._min_value_node(node.right)
            node.value = min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.value)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)