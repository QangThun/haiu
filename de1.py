
from collections import deque

def bfs_path(graph, start, goals):
    """Trả về đường đi ngắn nhất (theo số cạnh) từ start tới 1 nút bất kỳ trong goals.
    Nếu không có đường đi, trả về None.
    """
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        u = path[-1]
        if u in goals:
            return path
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(path + [v])
    return None

# Đồ thị suy ra từ đề 1
graph = {
    "A": ["B", "C", "D"],
    "B": ["H", "I"],
    "C": ["E", "F"],
    "F": ["J" , "K"],
    "D": ["G"],
}

if __name__ == "__main__":
    start = "A"
    goals = {"I", "G", "K"}
    path = bfs_path(graph, start, goals)
    print("Start:", start)
    print("Goals:", goals)
    print("Path found:", " -> ".join(path) if path else None)

    # Kiểm tra yêu cầu đề: phải xuất phát từ A và kết thúc ở 1 phần tử trong Goal
    assert path is not None, "Không tìm thấy đường đi tới tập Goal"
    assert path[0] == start, "Đường đi không bắt đầu từ A"
    assert path[-1] in goals, "Đỉnh kết thúc không thuộc Goal"

