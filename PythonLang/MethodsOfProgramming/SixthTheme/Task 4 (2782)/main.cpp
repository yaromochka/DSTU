#include <iostream>
#include <set>

class SortedList {
private:
    std::set<int> s;
    int lastQuery;

public:
    SortedList() : lastQuery(-1) {}

    void add(int x) {
        if (lastQuery != -1) {
            x = (x + lastQuery) % 1000000000;
        }
        s.insert(x);
        lastQuery = -1;
    }

    int next(int x) {
        auto it = s.lower_bound(x); // Находим первый элемент, не меньший x
        if (it != s.end()) {
            lastQuery = *it;
            return lastQuery;
        } else {
            lastQuery = -1;
            return -1;
        }
    }
};

int main() {
    int n;
    std::cin >> n;
    SortedList sortedList;

    for (int i = 0; i < n; ++i) {
        char operation;
        int x;
        std::cin >> operation >> x;
        if (operation == '+') {
            sortedList.add(x);
        } else if (operation == '?') {
            std::cout << sortedList.next(x) << std::endl;
        }
    }

    return 0;
}