#Kendrik Deleoz

from heapq import heappush, heappop

def prim(graph,start):
    visited= set()
    mst_edges = []
    total_cost = 0


    pq = []
    visited.add(start)

    for neighbor, weight in graph[start]:
        heappush(pq, (weight, start,neighbor))

    while pq:
        weight, u, v = heappop(pq)

        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u,v,weight))
        total_cost += weight
        

        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heappush(pq, (w,v,neighbor))
    
    return mst_edges, total_cost

if __name__ == "__main__":

    graph = {
        'A': [('B',4),('C',2),('D',3)],
        'B': [('A',4),('D',2)],
        'C': [('A',2),('D',4)],
        'D': [('A',3),('B',2),('C',4)]
    }
    
    start_node = 'A'
    mst, cost = prim(graph,start_node)

    print(f"Starting from {start_node}")
    print("Edges in Minimum Spanning Tree:")
    for u,v,w in mst:
        print(f" {u} -- {v} (weight {w})")
    
    print(f"Total MST Cost: {cost}")