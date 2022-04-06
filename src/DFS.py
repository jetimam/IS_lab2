def search(start, goal, graph):
    stack = []
    backtrack_table = {}
    visited = {}
    stack.append(start)
    n = 0
    while len(stack) > 0:
        current = stack.pop()
        n += 1
        visited[current] = True
        if current == goal:
            return [backtrack(start, current, backtrack_table), n]
        else:
            children = get_children(graph, current, visited)
            for child in children:
                stack.append(child)
                backtrack_table[child] = current

    return [[], n]

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