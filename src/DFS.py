def search(start, goal, graph):
    stack = []
    backtrack_table = {}
    visited = {}
    stack.append(start)
    found = False
    while not found and len(stack) > 0:
        current = stack.pop()
        visited[current] = True
        if current == goal:
            found = True
            return backtrack(start, current, backtrack_table)
        else:
            children = get_children(graph, current, visited)
            for child in children:
                stack.append(child)
                backtrack_table[child] = current

    return ['this is weird']

def get_children(graph, current, visited):
    children = []
    for child in graph[current]:
        if child not in visited:
            children.append(child)
    #children.reverse() to go on the left
    return children
        
def backtrack(start, current, backtrack_table):
    path = []
    while current != start:
        path.append(current)
        current = backtrack_table[current]
    path.append(start)
    path.reverse()
    return path