from queue import PriorityQueue

def search(start, goal, graph):
	priority_queue = PriorityQueue(0)
	backtrack_table = {}
	visited = {}
	priority_queue.put((0, start))
	n = 0
	while not priority_queue.empty():
		current = priority_queue.get()
		n += 1
		visited[current[1]] = True
		if current[1] == goal:
			return [backtrack(start, current[1], backtrack_table), n]
		else:
			children = get_children(graph, current, visited)
			for child in children:
				g_score = child[0] + current[0]
				priority_queue.put((g_score, child[1]))
				backtrack_table[child[1]] = current[1]
	return [[], n]

def get_children(graph, current, visited):
	children = []
	for child in graph[current[1]]:
		if child[0] not in visited:
			temp_child = child[::-1]
			children.append(temp_child)
	return children
		
def backtrack(start, current, backtrack_table):
	path = []
	while current != start:
		path.append(current)
		current = backtrack_table[current]
	path.reverse()
	return path