import sys

INF = 10**9  # Используем большое число вместо sys.maxsize


def floyd_warshall(n, flights):
    dist = [[INF] * n for _ in range(n)]
    parent = [[-1] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for idx, (u, v, w) in enumerate(flights):
        dist[u][v] = min(dist[u][v], -w)
        parent[u][v] = idx

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    parent[i][j] = parent[i][k]

    return dist, parent


def find_best_path(n, concerts, dist, parent, flights):
    for city in concerts:
        if dist[city][city] < 0:
            return "infinitely kind", []

    path = []
    for i in range(len(concerts) - 1):
        u, v = concerts[i], concerts[i + 1]
        while u != v:
            path.append(parent[u][v] + 1)
            u = flights[parent[u][v]][1]

    return len(path), path


def main():
    n, m, k = map(int, input().split())

    flights = []
    for i in range(m):
        u, v, w = map(int, input().split())
        flights.append((u - 1, v - 1, w))  # Приводим города к индексации с нуля

    concerts = list(map(int, input().split()))
    concerts = [c - 1 for c in concerts]  # Индексация с нуля

    dist, parent = floyd_warshall(n, flights)
    result, path = find_best_path(n, concerts, dist, parent, flights)

    if result == "infinitely kind":
        print(result)
    else:
        print(result)
        print(*path)


if __name__ == "__main__":
    main()
