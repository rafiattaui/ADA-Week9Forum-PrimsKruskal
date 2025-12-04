import time
import sys
import csv
from load_graph import load_graph
from save import save_to_csv 

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) 
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal_mst(edges, num_nodes):
    current_edges = sorted(edges, key=lambda x: x[2]) 

    dsu = DSU(num_nodes)
    mst_weight = 0.0
    mst_edge_count = 0
    mst_edges = []

    for u, v, weight in current_edges:
        if dsu.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            mst_edge_count += 1

            if mst_edge_count == num_nodes - 1:
                break
    
    if mst_edge_count < num_nodes - 1:
        print(f"Warning: Graph is likely disconnected. Found {mst_edge_count} edges, expected {num_nodes - 1} for a connected graph with {num_nodes} nodes.")
        
    return mst_edges, mst_weight

def preprocess_graph(adj_list):
    node_ids = sorted(list(adj_list.keys()))
    id_map = {node: i + 1 for i, node in enumerate(node_ids)}
    num_nodes = len(node_ids)

    unique_edges = set() 
    
    for u_str, neighbors in adj_list.items():
        u_int = id_map[u_str]
        for v_str, weight in neighbors:
            v_int = id_map[v_str]
            if u_int < v_int:
                unique_edges.add((u_int, v_int, weight))
            else:
                unique_edges.add((v_int, u_int, weight))

    edge_list = list(unique_edges)
    
    return edge_list, num_nodes


if __name__ == "__main__":
    
    FILE_PATH = "standard.text"
    GRAPH_NAME = "standard_Kruskal"
    NUM_RUNS = 10
    
    print(f"--- Kruskal's MST on {FILE_PATH} ---")
    
    adj_list = load_graph(FILE_PATH)
    
    if not adj_list:
        sys.exit("Graph loading failed. Check file path and format.")

    initial_edges, num_nodes = preprocess_graph(adj_list)
    print(f"Graph prepared: V={num_nodes}, E={len(initial_edges)}. Running {NUM_RUNS} times...")
    
    
    for run in range(1, NUM_RUNS + 1):
        startTime = time.time()
        
        kruskalMst, total_weight = kruskal_mst(initial_edges, num_nodes)
        
        endTime = time.time()
        
        execTime = endTime - startTime
        
        print(f"Run {run}: Time = {execTime:.6f} s, Total Weight = {total_weight}")

        save_to_csv(f"{GRAPH_NAME}_Run{run}", kruskalMst, total_weight, execTime)
    
    print("\nExecution complete. Results saved to mst_output.csv.")