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

start = 'A'
goal = 'P'

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()

        if node == goal:
            return path

        if node in visited:
            continue
        visited.add(node)

        # đảo ngược để đi từ trái sang phải giống hình
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    path = dfs(graph, start, goal)
    if path:
        print("Đường đi DFS từ", start, "tới", goal, ":", " -> ".join(path))
    else:
        print("Không tìm được đường đi")
