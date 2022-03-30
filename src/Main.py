import DFS, BFS, Dijkstra, AS, Graph
start = 'Arad'
goal = 'Bucharest'
print('DFS ->', DFS.search(start, goal, Graph.map))
print('BFS ->', BFS.search(start, goal, Graph.map))
print('Dijsktra ->', Dijkstra.search(start, goal, Graph.map))
euclidean = lambda sld, city: sld[city]
print('A* ->', AS.search(start, goal, Graph.map, Graph.sld, euclidean))