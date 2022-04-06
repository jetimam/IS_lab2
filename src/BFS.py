from queue import Queue

def search(start, goal, graph):
    queue = Queue(0)
    backtrack_table = {}
    visited = {}
    queue.put(start)
    n = 0
    while not queue.empty():
        current = queue.get()
        n += 1
        if current == goal:
            return [backtrack(start, current, backtrack_table), n]
        else:
            children = get_children(graph, current, visited)
            for child in children:
                queue.put(child)
                backtrack_table[child] = current
                visited[child] = True

    return [[], n]

def get_children(graph, current, visited):
    children = []
    for child in graph[current]:
        if child[0] not in visited:
            children.append(child[0])
    return children
        
def backtrack(start, current, backtrack_table):
    path = []
    while current != start:
        path.append(current)
        current = backtrack_table[current]
    path.reverse()
    return path