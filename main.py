import heapq
# part 1

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = {}

    def add_edge(self, edge_id, start_vertex, end_vertex, road_name, road_length):
        if start_vertex not in self.vertices:
            self.add_vertex(start_vertex)
        if end_vertex not in self.vertices:
            self.add_vertex(end_vertex)

        self.edges[edge_id] = {
            'start': start_vertex,
            'end': end_vertex,
            'name': road_name,
            'length': road_length
        }

        # Add edge to the vertices
        self.vertices[start_vertex][end_vertex] = edge_id
        self.vertices[end_vertex][start_vertex] = edge_id

    def print_graph(self):
        print("Vertices:")
        for vertex in self.vertices:
            print(f"ID: {vertex}")

        print("\nEdges:")
        for edge_id, edge_info in self.edges.items():
            print(
                f"ID: {edge_id}, Start: {edge_info['start']}, End: {edge_info['end']}, Name: {edge_info['name']}, Length: {edge_info['length']}")


# Example usage
if __name__ == "__main__":
    # Create a graph
    graph = Graph()

    # Add vertices
    for i in range(1, 41):  # Adding 40 vertices
        graph.add_vertex(i)

    # Add edges
    edges_info = [
        ("1-2", 1, 2, "Road_A", 5),
        ("2-3", 2, 3, "Road_B", 7),
        ("3-4", 3, 4, "Road_C", 6),
        ("4-5", 4, 5, "Road_D", 8),
        ("5-6", 5, 6, "Road_E", 9),
        ("6-7", 6, 7, "Road_F", 5),
        ("7-8", 7, 8, "Road_G", 7),
        ("8-9", 8, 9, "Road_H", 6),
        ("9-10", 9, 10, "Road_I", 8),
        ("1-10", 1, 10, "Road_J", 10),
        ("11-12", 11, 12, "Road_K", 7),
        ("12-13", 12, 13, "Road_L", 6),
        ("13-14", 13, 14, "Road_M", 8),
        ("14-15", 14, 15, "Road_N", 9),
        ("15-16", 15, 16, "Road_O", 5),
        ("16-17", 16, 17, "Road_P", 7),
        ("17-18", 17, 18, "Road_Q", 6),
        ("18-19", 18, 19, "Road_R", 8),
        ("19-20", 19, 20, "Road_S", 10),
        ("11-20", 11, 20, "Road_T", 5),
        ("21-22", 21, 22, "Road_U", 7),
        ("22-23", 22, 23, "Road_V", 6),
        ("23-24", 23, 24, "Road_W", 8),
        ("24-25", 24, 25, "Road_X", 9),
        ("25-26", 25, 26, "Road_Y", 5),
        ("26-27", 26, 27, "Road_Z", 7),
        ("27-28", 27, 28, "Road_AA", 6),
        ("28-29", 28, 29, "Road_AB", 8),
        ("29-30", 29, 30, "Road_AC", 10),
        ("21-30", 21, 30, "Road_AD", 5),
        ("31-32", 31, 32, "Road_AE", 7),
        ("32-33", 32, 33, "Road_AF", 6),
        ("33-34", 33, 34, "Road_AG", 8),
        ("34-35", 34, 35, "Road_AH", 9),
        ("35-36", 35, 36, "Road_AI", 5),
        ("36-37", 36, 37, "Road_AJ", 7),
        ("37-38", 37, 38, "Road_AK", 6),
        ("38-39", 38, 39, "Road_AL", 8),
        ("39-40", 39, 40, "Road_AM", 10),
        ("31-40", 31, 40, "Road_AN", 5),
    ]

    for edge_info in edges_info:
        graph.add_edge(*edge_info)

    # Print the graph
    graph.print_graph()
