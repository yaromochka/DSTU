"""
НЕ СДЕЛАНО
"""

import sys
from collections import OrderedDict
import bisect



class StockDatabase:
    def __init__(self):
        self.stocks = OrderedDict()  # {code: (id, reliability)}
        self.id_counter = 0
        self.sorted_stocks = []  # [(reliability, id, code)]

    def issue(self, code):
        """Добавляет новую ценную бумагу или возвращает её данные, если уже существует"""
        if code in self.stocks:
            stock_id, reliability = self.stocks[code]
            print(f"EXISTS {stock_id} {reliability}")
        else:
            stock_id = self.id_counter
            self.id_counter += 1
            self.stocks[code] = (stock_id, 0)
            bisect.insort(self.sorted_stocks, (0, stock_id, code))
            print(f"CREATED {stock_id} 0")

    def delete(self, code):
        """Удаляет ценную бумагу из базы"""
        if code in self.stocks:
            stock_id, reliability = self.stocks.pop(code)
            self.sorted_stocks.remove((reliability, stock_id, code))
            print(f"OK {stock_id} {reliability}")
        else:
            print("BAD REQUEST")

    def reliability(self, code, value):
        """Изменяет надежность указанной ценной бумаги"""
        if code in self.stocks:
            stock_id, old_reliability = self.stocks[code]
            self.sorted_stocks.remove((old_reliability, stock_id, code))
            new_reliability = old_reliability + value
            self.stocks[code] = (stock_id, new_reliability)
            bisect.insort(self.sorted_stocks, (new_reliability, stock_id, code))
            print(f"OK {stock_id} {new_reliability}")
        else:
            print("BAD REQUEST")

    def find(self, n):
        """Находит ценную бумагу на n-м месте в упорядоченном списке"""
        if not self.sorted_stocks:
            print("EMPTY")
        else:
            index = min(n, len(self.sorted_stocks) - 1)
            reliability, stock_id, code = self.sorted_stocks[-(index + 1)]
            print(f"OK {code} {stock_id} {reliability}")


def main():
    db = StockDatabase()
    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        command = sys.stdin.readline().strip().split()

        if command[0] == "ISSUE":
            db.issue(command[1])
        elif command[0] == "DELETE":
            db.delete(command[1])
        elif command[0] == "RELIABILITY":
            db.reliability(command[1], int(command[2]))
        elif command[0] == "FIND":
            db.find(int(command[1]))


if __name__ == "__main__":
    main()
