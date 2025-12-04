def load_graph(file_path):
    # graphs are represented as adjacency lists in the file:
    # (source) (destination) (distance) per line

    graph = {}
    with open(file_path, 'r') as f:
        for line in f:
            _, source, destination, distance = line.strip(" ").split()
            graph[source] = graph.get(source, []) + [(destination, int(distance))]
            graph[destination] = graph.get(destination, []) + [(source, int(distance))]
    return graph

if __name__ == "__main__":
    graph = load_graph("USA-road-d.FLA.text")
    for node, edges in graph.items():
        print(f"{node}: {edges}")