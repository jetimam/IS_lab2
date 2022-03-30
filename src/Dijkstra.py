from queue import PriorityQueue
import sys

def search(start, goal, graph):
	priority_queue = PriorityQueue(0)
	backtrack_table = {}
	visited = {}
	priority_queue.put((0, start))
	while not priority_queue.empty():
		current = priority_queue.get()
		visited[current[1]] = True
		if current[1] == goal:
			return backtrack(start, current[1], backtrack_table)
		else:
			children = get_children(graph, current, visited)
			for child in children:
				g_score = child[0] + current[0]
				# print(child[1], '->', g_score)
				priority_queue.put((g_score, child[1]))
				backtrack_table[child[1]] = current[1]
	return []

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