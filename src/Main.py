import DFS
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
print(DFS.search(start,goal,graph))