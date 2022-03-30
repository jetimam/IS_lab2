import DFS, BFS, Graph
start = 'Arad'
goal = 'Bucharest'
print('DFS path ->', DFS.search(start,goal,Graph.map))
print('BFS path ->', BFS.search(start,goal,Graph.map))