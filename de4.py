
import heapq

def astar(graph, h, start, goal):
    """A* trả về (đường đi, tổng chi phí)."""
    open_heap = [(h[start], 0, start, [start])]  # (f, g, node, path)
    best_g = {start: 0}
    while open_heap:
        f, g, u, path = heapq.heappop(open_heap)
        if u == goal:
            return path, g
        for v, w in graph.get(u, []):
            new_g = g + w
            if new_g < best_g.get(v, float("inf")):
                best_g[v] = new_g
                heapq.heappush(open_heap, (new_g + h.get(v, 0), new_g, v, path + [v]))
    return None, float("inf")

# Cạnh có trọng số theo đề 2 (suy từ hình)
graph = {
    "B": [("J", 2), ("C", 12), ("E", 2)],
    "J": [("I", 2),  ("IH", 2)],
    "C": [("D", 2), ("F", 3)],
    "E": [("G", 3)],
    "F": [("A", 6), ("K", 3)],
}

# Heuristic h(n) (giá trị trên hình, A=0)
h = {"A":0, "B":12, "C":8, "D":7, "E":2, "F":4, "G":3, "K":6, "J":1, "I":3, "IH":2}

if __name__ == "__main__":
    start, goal = "B", "A"
    path, cost = astar(graph, h, start, goal)
    print("Start:", start, "| Goal:", goal)
    print("Path found:", " -> ".join(path) if path else None)
    print("Total cost:", cost)

    # Kiểm tra yêu cầu đề: phải về đích A và chi phí là tổng trọng số cạnh
    assert path is not None, "Không tìm thấy đường đi"
    assert path[0] == start and path[-1] == goal, "Đường đi không đúng start/goal"