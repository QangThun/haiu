import heapq

# Đồ thị có trọng số đề 4
graph = {
    'B': {'J': 2, 'C': 12, 'E': 2},
    'J': {'I': 2, 'H': 6},
    'C': {'D': 2, 'F': 3},
    'E': {'G': 3},
    'F': {'A': 6, 'K': 3},
    'I': {}, 'H': {}, 'D': {}, 'G': {}, 'A': {}, 'K': {}
}

# heuristic h(n) ở cạnh mỗi nút
h = {
    'B': 12, 'J': 1, 'I': 3, 'H': 2,
    'C': 8, 'D': 7, 'F': 4,
    'E': 2, 'G': 3,
    'A': 0, 'K': 6,
}

start = 'B'
goal = 'A'

def a_star(graph, h, start, goal):
    # phần tử: (f, g, node, path)
    open_heap = [(h[start], 0, start, [start])]
    best_g = {}

    while open_heap:
        f, g, node, path = heapq.heappop(open_heap)

        if node == goal:
            return path, g

        if node in best_g and g >= best_g[node]:
            continue
        best_g[node] = g

        for neighbor, cost in graph[node].items():
            new_g = g + cost
            new_f = new_g + h[neighbor]
            heapq.heappush(open_heap,
                           (new_f, new_g, neighbor, path + [neighbor]))

    return None, None

if __name__ == "__main__":
    path, cost = a_star(graph, h, start, goal)
    if path:
        print("Đường đi A* từ", start, "tới", goal, ":", " -> ".join(path))
        print("Tổng chi phí:", cost)
    else:
        print("Không tìm được đường đi")
