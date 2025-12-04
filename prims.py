from load_graph import load_graph
from save import save_to_csv
import time

def prims(graph, start_node=0):
    import heapq

    visited  = set()
    mst = []
    total_weight = 0
    min_heap = []

    start = (0, start_node, None)  # (weight, current_node, from_node)
    heapq.heappush(min_heap, start)

    while min_heap:
        weight, current_node, from_node = heapq.heappop(min_heap)
        print(f"Visiting node: {current_node} with edge weight: {weight}")

        if current_node in visited:
            continue

        visited.add(current_node)
        total_weight += weight
        if from_node is not None:
            mst.append((from_node, current_node, weight))

        for neighbor, edge_weight in graph.get(current_node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor, current_node))
        
    return mst, total_weight

if __name__ == "__main__":
    graph = load_graph("USA-road-d.FLA.text")

    for _ in range(10):

        startTime = time.time()

        primsMst, total_weight = prims(graph, start_node='1')

        endTime = time.time()

        execTime = endTime - startTime
        execTime = round(execTime, 6)

        save_to_csv("USA-road-d.FLA", primsMst, total_weight, execTime)
    
    
    
