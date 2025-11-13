from collections import deque

# Đồ thị đề 1 (theo hình)
graph = {
    'A': ['D', 'N', 'K'],
    'D': ['G'],
    'N': ['S', 'P'],
    'K': ['Z'],
    'G': [],
    'S': ['T', 'C'],
    'P': [],
    'Z': ['B', 'M'],
    'T': [],
    'C': [],
    'B': [],
    'M': [],
}

start = 'A'   # To
goal = 'P'    # Tg

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    path = bfs(graph, start, goal)
    if path:
        print("Đường đi BFS từ", start, "tới", goal, ":", " -> ".join(path))
    else:
        print("Không tìm được đường đi")
