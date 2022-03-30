import DFS, BFS, Dijkstra, Graph
start = 'Arad'
goal = 'Bucharest'
print('DFS ->', DFS.search(start,goal,Graph.map))
print('BFS ->', BFS.search(start,goal,Graph.map))
print('Dijsktra ->', Dijkstra.search(start,goal,Graph.map))