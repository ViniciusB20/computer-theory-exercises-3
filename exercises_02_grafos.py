#Exercicio 2 - Lista 3
import networkx as nx
import matplotlib.pyplot as plt
 
G = nx.Graph()
 
# Adicionar Vertices
G.add_node("v0")
G.add_node("v1")
G.add_node("v2")
G.add_node("v3")
G.add_node("v4")
G.add_node("v5")
G.add_node("v6")
G.add_node("v7")
 
# Adicioar Arestas
G.add_edge("v0","v2")
G.add_edge("v1","v2")
G.add_edge("v2","v3")
G.add_edge("v3","v4")
G.add_edge("v4","v5")
G.add_edge("v5","v6")
G.add_edge("v2","v4")
G.add_edge("v0","v6")
G.add_edge("v6","v7")
 
# Listar Vértices 
print("Vertices:")
print(G.nodes())
 
print("")
print('*' *60)
 
# Listar Arestas
print('Arestas:')
for arestas in G.edges():
  print(arestas)
 
print("")
print('*' *60)
 
# Listar Graus
print('Graus Do Grafo:')
for graus in G.degree():
  print(graus)
 
print("")
print('*' *60)
 
# Matriz De Vizinhos
print('Matriz De Vizinhos:')
M = nx.adjacency_matrix(G)
print(M.todense()) 
 
# Adicionar Peso Para Cada Aresta
G["v1"]["v2"]['peso'] = 9
G["v2"]["v3"]['peso'] = 8
G["v3"]["v4"]['peso'] = 7
G["v4"]["v5"]['peso'] = 6
G["v5"]["v6"]['peso'] = 5
G["v2"]["v4"]['peso'] = 4
G["v0"]["v6"]['peso'] = 3
G["v6"]["v7"]['peso'] = 2
G["v0"]["v2"]['peso'] = 1
 
print("")
print('*' *60)
 
# Listar Arestas e Pesos
print('Arestas e Pesos:')
for edge in G.edges():
  u = edge[0]
  v = edge[1]
  print('Peso', edge,'valor', G[u][v]['peso'])
 
print("")
print('*' *60)
 
# Grafo Imagem
print('Grafo Imagem:')
plt.figure(1)
nx.draw(G,pos=nx.spring_layout(G),with_labels=True)
plt.show()
