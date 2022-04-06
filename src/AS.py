from queue import PriorityQueue

def search(start, goal, graph, sld, heuristic):
	priority_queue = PriorityQueue(0)
	backtrack_table = {}
	visited = {}
	visited[start] = True
	priority_queue.put((heuristic(sld, start), (0, start)))
	n = 0
	while not priority_queue.empty():
		current = priority_queue.get()
		n += 1
		visited[current[1][1]] = True
		if current[1][1] == goal:
			return [backtrack(start, current[1][1], backtrack_table), n]
		else:
			children = get_children(graph, current, visited)
			for child in children:
				g_score = current[1][0] + child[0]
				h_score = heuristic(sld, child[1])
				f_score = g_score + h_score
				backtrack_table[child[1]] = current[1][1]
				priority_queue.put((f_score, (g_score, child[1])))
	return [[], n]

def get_children(graph, current, visited):
	children = []
	for child in graph[current[1][1]]:
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