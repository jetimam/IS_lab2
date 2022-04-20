import DFS, BFS, Dijkstra, AS, Graph
import time

start = 'Arad'
goal = 'Bucharest'
start_time = time.time()
DFS_data = DFS.search(start, goal, Graph.map)
DFS_time = time.time() - start_time
print("DFS Path: " + str(DFS_data[0]) + " | Execution Time: " + str(DFS_time) +  " | Path Length: " + str(len(DFS_data[0])) + " | Total Expanded Nodes: " + str(DFS_data[1]))
print("DFS complexity: O(V) + O(E) where E is the number of edges, and V is the number of vertices.\n")

start_time = time.time()
BFS_data = BFS.search(start, goal, Graph.map)
BFS_time = time.time() - start_time
print("BFS Path: " + str(BFS_data[0]) + " | Execution Time: " + str(BFS_time) +  " | Path Length: " + str(len(BFS_data[0])) + " | Total Expanded Nodes: " + str(BFS_data[1]))
print("BFS complexity: O(V) + O(E) where E is the number of edges, and V is the number of vertices.\n")


start_time = time.time()
Dijkstra_data = Dijkstra.search(start, goal, Graph.map)
Dijkstra_time = time.time() - start_time
print("Dijkstra Path: " + str(Dijkstra_data[0]) + " | Execution Time: " + str(Dijkstra_time) +  " | Path Length: " + str(len(Dijkstra_data[0])) + " | Total Expanded Nodes: " + str(Dijkstra_data[1]))
print("Dijkstra complexity: O(V^2) where V is the amount of vertices\n")

start_time = time.time()
euclidean = lambda sld, city: sld[city]
AS_data = AS.search(start, goal, Graph.map, Graph.sld, euclidean)
AS_time = time.time() - start_time
print("A* Path: " + str(AS_data[0]) + " | Execution Time: " + str(AS_time) +  " | Path Length: " + str(len(AS_data[0])) + " | Total Expanded Nodes: " + str(AS_data[1]))
print("A* complexity: O(b^d) where b is the branching factor and d is the depth of the goal node")