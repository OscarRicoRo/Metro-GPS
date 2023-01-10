# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ob = search.GPSProblem('O', 'B', search.romania)

print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(ab).path())
print("Búsqueda en profundidad:")
print(search.depth_first_graph_search(ab).path())

print("Branch and bound: (AB)")
print(search.branch_and_bound(ab).path())
print("Branch and bound con heuristica: (AB)")
print(search.branch_and_bound_with_heuristic(ab).path())

print("Branch and bound: (OB)")
print(search.branch_and_bound(ob).path())
print("Branch and bound con heuristica: (OB)")
print(search.branch_and_bound_with_heuristic(ob).path())

# Result:
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101 + 138 + 120 + 75  + 70 + 111 + 118= 733
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
