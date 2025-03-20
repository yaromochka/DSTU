"""
НЕ РАБОТАЕТ
"""

import sys

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [False] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        """Построение дерева отрезков."""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def push(self, node, start, end):
        """Применение отложенного переворота."""
        if self.lazy[node]:
            self.lazy[node] = False
            if start != end:  # Если не лист
                self.lazy[2 * node + 1] ^= True
                self.lazy[2 * node + 2] ^= True

    def range_reverse(self, L, R):
        """Перевернуть отрезок [L, R]."""
        self._update(0, 0, self.n - 1, L, R)

    def _update(self, node, start, end, L, R):
        self.push(node, start, end)

        if start > R or end < L:
            return
        if L <= start and end <= R:
            self.lazy[node] ^= True
            self.push(node, start, end)
            return

        mid = (start + end) // 2
        self._update(2 * node + 1, start, mid, L, R)
        self._update(2 * node + 2, mid + 1, end, L, R)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def range_min(self, L, R):
        """Минимум на отрезке [L, R]."""
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        self.push(node, start, end)

        if start > R or end < L:
            return float('inf')
        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        left_res = self._query(2 * node + 1, start, mid, L, R)
        right_res = self._query(2 * node + 2, mid + 1, end, L, R)

        return min(left_res, right_res)


def main():
    input = sys.stdin.read
    data = input().splitlines()

    # Чтение входных данных
    n, m = map(int, data[0].split())
    arr = list(map(int, data[1].split()))

    # Построение дерева отрезков
    seg_tree = SegmentTree(arr)

    # Обработка запросов
    result = []
    for i in range(2, 2 + m):
        query = list(map(int, data[i].split()))
        L, R = query[1] - 1, query[2] - 1  # Приводим к 0-индексации
        if query[0] == 1:
            seg_tree.range_reverse(L, R)
        else:
            result.append(str(seg_tree.range_min(L, R)))

    # Вывод результата
    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
