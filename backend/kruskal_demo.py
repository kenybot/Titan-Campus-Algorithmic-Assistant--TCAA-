#kendrik deleoz

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            return True
        return False
    
def kruskal(nodes, edges):
    edges.sort()
    dsu = DSU(len(nodes))
    index = { node: i for i , node in enumerate(nodes)}
    mst_edges = []
    total_cost = 0

    for weight, u , v in edges:
        if dsu.union(index[u],index[v]):
            mst_edges.append((u, v, weight))
            total_cost += weight
    return mst_edges, total_cost

if __name__ == "__main__":
    nodes = ['A','B','C', 'D']
    edges = [
        (4,'A','B'),
        (2,'A','C'),
        (3,'A','D'),
        (2,'B','D'),
        (4,'C','D')
    ]

    mst , cost = kruskal(nodes, edges)
    print("Edges in MST: ")
    for u,v,w in mst:
        print(f"  {u} -- {v}  (weight {w})")
    
    print(f"Total MST Cost: {cost}")