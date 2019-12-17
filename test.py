from DM_Library import Graph

G1_graph = {1: [3, 6], 2: [3, 6], 3: [1,2,6], 6: [1,2,3] }
G1 = Graph(G1_graph)
# print(G1)
# print(G1.get_links())
# print(G1.getGraphDict())
G1.add_link((6,2))
G1.add_link((6,2))
G1.add_link((6,2))
G1.add_link((4,4))
# print(G1)
print(G1.getGraphDict())
G1.add_node(4)

# print(G1.getGraphDict())
print(G1.get_all_adjacencies())
print(G1)
print(G1.getGraphDict())
G1.add_node(4)

print(G1.get_node_adjacencies(6))
