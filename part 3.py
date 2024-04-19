import heapq


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


class GraphWithHouses(Graph):
    def __init__(self):
        super().__init__()
        self.houses = {}

    def add_house(self, house_id, intersection_id, distance_to_intersection):
        if intersection_id not in self.vertices:
            raise ValueError("Intersection not found")

        self.houses[house_id] = {'intersection': intersection_id, 'distance': distance_to_intersection}
        self.vertices[house_id] = {'type': 'house', 'distance': distance_to_intersection}
        self.vertices[intersection_id][house_id] = 'house'

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_vertex] = 0
        queue = [(0, start_vertex)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, edge_id in self.vertices[current_vertex].items():
                if neighbor == 'type':  # Skip 'type' key
                    continue

                if 'house' in self.vertices[current_vertex] and self.vertices[current_vertex]['type'] == 'house':
                    distance = current_distance + self.houses[neighbor]['distance']
                else:
                    distance = current_distance + self.edges[edge_id]['length']

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

    def shortest_path(self, start_vertex, end_vertex):
        distances = self.dijkstra(start_vertex)
        path = [end_vertex]

        while end_vertex != start_vertex:
            for neighbor, edge_id in self.vertices[end_vertex].items():
                if 'house' in self.vertices[neighbor] and self.vertices[neighbor]['type'] == 'house':
                    distance = distances[neighbor] - self.houses[neighbor]['distance']
                else:
                    distance = distances[neighbor] - self.edges[edge_id]['length']

                if distance == distances[end_vertex] - 1:
                    path.append(neighbor)
                    end_vertex = neighbor
                    break

        return path[::-1]


# Example usage
if __name__ == "__main__":
    # Create a graph with houses
    graph = GraphWithHouses()

    # Add vertices
    for i in range(1, 41):
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

    # Add houses
    houses_info = [
        (41, 1, 3),
        (42, 10, 4),
        (43, 20, 5),
        (44, 2, 2),
        (45, 5, 3),
        (46, 15, 4),
        (47, 25, 3),
        (48, 30, 5),
        (49, 8, 2),
        (50, 12, 4),
        (51, 18, 3),
        (52, 22, 2),
        (53, 28, 4),
        (54, 35, 3),
        (55, 37, 5),
        (56, 39, 2),
        (57, 4, 4),
        (58, 7, 3),
        (59, 11, 5),
        (60, 14, 2),
        (61, 16, 3),
        (62, 19, 4),
        (63, 21, 5),
        (64, 23, 2),
        (65, 26, 4),
        (66, 29, 3),
        (67, 32, 5),
        (68, 34, 2),
        (69, 36, 3),
        (70, 38, 4),
        (71, 40, 5),
    ]


    for house_info in houses_info:
        graph.add_house(*house_info)

    # Find shortest path between two intersections
    start_vertex = 1
    end_vertex = 40
    shortest_path = graph.shortest_path(start_vertex, end_vertex)

    # Print shortest path
    print(f"Shortest path from vertex {start_vertex} to vertex {end_vertex}: {' -> '.join(map(str, shortest_path))}")

''' part 4 complexity ( T(n) and O(n) ) analysis for the algorithms

Time Complexity T(n)

Initialization of Distances: Initializing distances for all vertices takes O(V) time, where 
V is the number of vertices.
Priority Queue Operations: The while loop runs for all vertices, and in each iteration, we perform heap operations which 
take O(logV) time. Therefore, the overall time complexity for priority queue operations is O(VlogV).
Edge and House Distance Updates: For each vertex, we update distances for its neighbors. In the worst case, each edge 
and house distance is processed once, resulting in O(E+H) time complexity, where E is the number of edges and H is the number of houses.
Total Time Complexity: Combining the above, the total time complexity for Dijkstra's algorithm is O(VlogV+E+H).

Space Complexity O(n)

Distances Dictionary: We use a dictionary to store distances for all vertices, which requires O(V) space.
Priority Queue: The priority queue can store up to 
V vertices, resulting in (V) space.
Total Space Complexity: Therefore, the total space complexity is O(V).
'''
