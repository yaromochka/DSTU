#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

/**
 * Функция для подсчета количества разбиений каждого числа на сумму двух других чисел из массива.
 */
vector<int> countPartitions(const vector<int>& numbers) {
    unordered_map<int, long long> countMap;

    // Подсчет количества вхождений каждого числа
    for (int num : numbers) {
        countMap[num]++;
    }

    vector<int> results(numbers.size());

    for (size_t i = 0; i < numbers.size(); i++) {
        int number = numbers[i];
        int count = 0;

        for (const auto& entry : countMap) {
            int x = entry.first;
            int y = number - x;

            // Избегаем дублирования (считаем только когда y >= x)
            if (y < x) continue;

            long long xCount = entry.second;

            if (x == y) {
                // Если x и y одинаковые, то выбираем 2 из countMap[x]
                count += xCount * (xCount - 1) / 2;
            } else if (countMap.count(y)) {
                // Если x и y разные, перемножаем их количества
                count += xCount * countMap[y];
            }
        }

        results[i] = count;
    }

    return results;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);

    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    vector<int> partitions = countPartitions(numbers);

    for (int result : partitions) {
        cout << result << endl;
    }

    return 0;
}
