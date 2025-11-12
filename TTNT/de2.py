
from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        u = path[-1]
        if u == goal:
            return path
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(path + [v])
    return None

# Đồ thị có hướng từ đề 4
graph = {
    "A": ["B", "N", "C"],
    "B": ["E", "F"],
    "N": ["P"],
    "C": ["G"],
    "E": ["H"],
    "P": ["K"],
    "G": ["D", "M"],
}

if __name__ == "__main__":
    start, goal = "A", "D"
    path = bfs_path(graph, start, goal)
    print("Start:", start, "| Goal:", goal)
    print("Path found:", " -> ".join(path) if path else None)

    # Kiểm tra yêu cầu đề
    assert path is not None, "Không tìm thấy đường đi"
    assert path[0] == start and path[-1] == goal, "Đường đi không đúng start/goal"
