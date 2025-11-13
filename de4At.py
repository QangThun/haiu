import heapq

# Đồ thị đề 4 (dùng lại như A*)
graph = {
    'B': {'J': 2, 'C': 12, 'E': 2},
    'J': {'I': 2, 'H': 6},
    'C': {'D': 2, 'F': 3},
    'E': {'G': 3},
    'F': {'A': 6, 'K': 3},
    'I': {}, 'H': {}, 'D': {}, 'G': {}, 'A': {}, 'K': {}
}

h = {
    'B': 12, 'J': 1, 'I': 3, 'H': 2,
    'C': 8, 'D': 7, 'F': 4,
    'E': 2, 'G': 3,
    'A': 0, 'K': 6,
}

start = 'B'
goal = 'A'

def greedy_best_first(graph, h, start, goal):
    # chỉ dùng heuristic h(n)
    open_heap = [(h[start], start, [start])]
    visited = set()

    while open_heap:
        heur, node, path = heapq.heappop(open_heap)

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph[node].keys():
            heapq.heappush(open_heap,
                           (h[neighbor], neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    path = greedy_best_first(graph, h, start, goal)
    if path:
        print("Đường đi At từ", start, "tới", goal, ":", " -> ".join(path))
    else:
        print("Không tìm được đường đi")
