import heapq

def min_fuel_cost(n, fuel_costs, roads):
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    INF = float('inf')
    pq = [(0, 0, 0, 0)]  # (cost, city, fuel, canister)
    visited = set()

    while pq:
        cost, city, fuel, canister = heapq.heappop(pq)

        if city == n - 1:
            return cost

        if (city, fuel, canister) in visited:
            continue
        visited.add((city, fuel, canister))

        # Заправка только бака
        if fuel == 0:
            heapq.heappush(pq, (cost + fuel_costs[city], city, 1, canister))

        # Заправка бака и канистры
        if fuel == 0 and canister == 0:
            heapq.heappush(pq, (cost + 2 * fuel_costs[city], city, 1, 1))

        # Переливание бензина из канистры в бак
        if fuel == 0 and canister:
            heapq.heappush(pq, (cost, city, 1, 0))

        # Переход в соседний город
        if fuel > 0:
            for neighbor in graph[city]:
                heapq.heappush(pq, (cost, neighbor, fuel - 1, canister))

    return -1  # Если путь не найден

# Чтение входных данных
n = int(input())
fuel_costs = list(map(int, input().split()))
m = int(input())
roads = [tuple(map(int, input().split())) for _ in range(m)]

# Вывод результата
print(min_fuel_cost(n, fuel_costs, roads))
