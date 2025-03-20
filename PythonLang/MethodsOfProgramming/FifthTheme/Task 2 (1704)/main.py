from collections import deque
from dataclasses import dataclass
from typing import List, Tuple, cast


@dataclass
class Road:
    from_city: int
    to_city: int
    from_gate: int
    to_gate: int
    visited: bool = False


class CityGraph:
    def __init__(self, n: int, roads_data: List[Tuple[int, int]]) -> None:
        self.n = n
        self.roads: List[Road] = []
        self.graph: List[List[int]] = [[] for _ in range(n + 1)]

        # Заполняем граф и список дорог
        for gate1, gate2 in roads_data:
            from_city = (gate1 + 3) // 4
            to_city = (gate2 + 3) // 4
            road_index = len(self.roads)
            self.graph[from_city].append(road_index)
            self.graph[to_city].append(road_index)
            self.roads.append(Road(from_city, to_city, gate1, gate2))

    def mark_road_visited(self, road_index: int) -> None:
        self.roads[road_index].visited = True

    def __getitem__(self, city: int) -> List[int]:
        return self.graph[city]


def can_complete_task(n: int, graph: CityGraph) -> List[int]:
    stack = deque()  # Используем deque как стек
    ans = []  # Список ворот
    cur_city = 1

    while True:
        if not graph[cur_city]:
            if not stack:
                break
            # Возвращаемся к предыдущему городу
            to_gate, from_gate, prev_city = (stack.pop() for _ in range(3))
            ans.extend((to_gate, from_gate))
            cur_city = prev_city
            continue

        road_index = graph[cur_city][-1]

        # Если дорога уже посещена
        if graph.roads[road_index].visited:
            graph[cur_city].pop()
            continue

        # Обновляем состояние дороги и перемещаемся в соседний город
        if cur_city == graph.roads[road_index].from_city:
            stack.extend([cur_city, graph.roads[road_index].from_gate, graph.roads[road_index].to_gate])
            graph.mark_road_visited(road_index)
            cur_city = graph.roads[road_index].to_city
        else:
            stack.extend([cur_city, graph.roads[road_index].to_gate, graph.roads[road_index].from_gate])
            graph.mark_road_visited(road_index)
            cur_city = graph.roads[road_index].from_city

    # Проверяем, удалось ли пройти через все ворота
    return ans if len(ans) == 4 * n else []


def main() -> None:
    n: int = int(input())

    roads_data: List[Tuple[int, int]] = cast(
        List[Tuple[int, int]],
        [tuple(map(int, input().split())) for _ in range(2 * n)]
    )

    graph = CityGraph(n, roads_data)

    result = can_complete_task(n, graph)

    if result:
        print("Yes", " ".join(map(str, result)), sep="\n")
    else:
        print("No")


if __name__ == "__main__":
    main()