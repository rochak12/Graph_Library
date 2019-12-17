from DMLibrary import Graph

G1_graph = {1: [3, 6], 2: [6, 3], 3: [1, 2], 6: [1,2] }
G1 = Graph(G1_graph)
# print(G1)
print(G1.get_links())
print(G1.get_nodes())
print(G1.get_spanning_tree(), end="\n\n")

""""""""""""""""""
g1 = {1: [2], 2:[1]}
g1 = Graph(g1)
print((g1.get_nodes()))
print(g1.get_links())
print(g1.get_spanning_tree(), end="\n\n")

""""""""""""""""""
g2 = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
g2 = Graph(g2)
print(g2.get_nodes())
print(g2.get_links())
print(g2.get_spanning_tree(), end="\n\n")

""""""""""""""
g3 = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3, 6], 5: [3, 6], 6: [4, 5]}
g3 = Graph(g3)
print(g3.get_nodes())
print(g3.get_links())
print(g3.get_spanning_tree(), end="\n\n")

""""""""""""""""""
g4 = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3, 6], 5: [3, 6, 7], 6: [4, 5, 8], 7: [5, 8], 8: [6, 7]}
g4 = Graph(g4)
print(g4.get_nodes())
print(g4.get_links())
print(g4.get_spanning_tree(), end="\n\n")


""""""""
g5 = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3, 6], 5: [3, 6, 7], 6: [4, 5, 8], 7: [5, 8, 9], 8: [6, 7, 10],
      9: [7, 10], 10: [9, 8]}
g5 = Graph(g5)
print(g5.get_nodes())
print(g5.get_links())
print(g5.get_spanning_tree(), end="\n\n")

""""""""
gt = {1: [2, 16, 17], 2: [1, 3, 4], 3: [2, 4, 5, 17], 4: [2, 3, 7], 5: [3, 6, 8, 10],
      6: [5, 7, 10], 7: [4, 6], 8: [5, 9, 11, 13], 9: [8, 10, 11], 10: [5, 6, 9], 11: [8, 9, 12],
      12: [11, 13, 14], 13: [8, 12, 14, 17], 14: [12, 13, 15], 15: [14, 16, 17], 16: [1, 15],
      17: [1, 3, 13, 15]}
gt = Graph(gt)
print(gt.get_nodes())
print(gt.get_links())
print(gt.get_spanning_tree(), end="\n\n")





#####################################################
""""""""""""""""""""""""""""""""""""""""""""""""""

from DMLibrary import Huffman
s1 = "knlnclnac"
code = Huffman.encode_text(s1)
print("\n\n", Huffman.decode_text(code))



# with open('listfile.txt', 'w') as filehandle:
#     for listitem in (primes(0, 179424674)):
#         filehandle.write('%s\n' % listitem)


#It is for reading from file
# places = []
#
# # open file and read the content in a list
# with open('listfile.txt', 'r') as filehandle:
#     for line in filehandle:
#         # remove linebreak which is the last character of the string
#         currentPlace = line[:-1]
#
#         # add item to the list
#         places.append(currentPlace)
