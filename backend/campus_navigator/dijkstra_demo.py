#kendrik deleoz

from heapq import heappush, heappop

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    parent = {start: None}

    pq = []
    heappush(pq, (0,start))
    visited = set()

    while pq: #while the list is not empty
        current_dist, u = heappop(pq) 
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph[u]:
            if v in visited:
                continue
            new_dist = current_dist + w

            if new_dist < distances[v]:
                distances[v] = new_dist
                parent[v] = u
                heappush(pq, (new_dist, v))

    return distances, parent

def rebuild_path(parent, target):
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    
    path.reverse()
    return path

#demo

if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C',2)],
        'B': [('A',4), ('C', 3), ('D',2)],
        'C': [('A',2),('B',3),('D',4),('E',5)],
        'D': [('B',2),('C',4),('E',1)],
        'E': [('C',5),('D',1)]
    }

    source = 'A'
    distances, parent = dijkstra(graph,source)

    print(f"Shortest distances from {source}:")
    for node in sorted(graph.keys()):
        d = distances[node]
        path = rebuild_path(parent,node) if d != float('inf') else []
        path_str = " -> ".join(path) if path else "(no path)"
        d_str = "inf" if d == float('inf') else str(d)
        print(f"{source} to {node}: distance = {d_str}, path = {path_str}")
