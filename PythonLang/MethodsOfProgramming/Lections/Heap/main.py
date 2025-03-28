class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_value

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Куча пуста")
        return self.heap[0]

    def heapify(self, array):
        self.heap = array[:]
        for i in range(len(self.heap) // 2, -1, -1):
            self._sift_down(i)

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

    def __str__(self):
        return str(self.heap)

def main() -> None:
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(8)
    heap.push(1)
    heap.push(2)

    print("Куча после вставки:", heap)

    print("Минимальный элемент:", heap.pop())
    print("Куча после pop:", heap)

    array = [1, 2, 8, 5, 3]
    heap.heapify(array)
    print("Куча после heapify:", heap)


if __name__ == "__main__":
    main()