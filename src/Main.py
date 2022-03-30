import graphlib
from Graph import Graph

graph = Graph(5)
graph.initialize()
graph.draw()
spawn_point = graph.get_spawn_point()
print('spawn point ->', spawn_point)
print('destination point ->', graph.get_destination())