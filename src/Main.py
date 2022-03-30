import DFS
import BFS
graph = {
	'A' : ['D', 'B', 'F'],
	'B' : ['D', 'C'],
	'C' : ['E', 'B'],
	'D' : ['A', 'G'],
	'E' : ['F', 'G'],
	'F' : ['B', 'C'],
	'G' : ['C']
}
start = 'A'
goal = 'E'
print('DFS path ->', DFS.search(start,goal,graph))
print('BFS path ->', BFS.search(start,goal,graph))