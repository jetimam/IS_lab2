from queue import Queue

def search(start, goal, graph):
    queue = Queue(0)
    backtrack_table = {}
    visited = {}
    queue.put(start)
    found = False
    while not found and not queue.empty():
        current = queue.get()
        if current == goal:
            found = True
            return backtrack(start, current, backtrack_table)
        else:
            children = get_children(graph, current, visited)
            for child in children:
                queue.put(child)
                backtrack_table[child] = current
                visited[child] = True

    return []

def get_children(graph, current, visited):
    children = []
    for child in graph[current]:
        if child[0] not in visited:
            children.append(child[0])
    #children.reverse() to go on the left
    return children
        
def backtrack(start, current, backtrack_table):
    path = []
    while current != start:
        path.append(current)
        current = backtrack_table[current]
    path.reverse()
    return path