from collections import defaultdict
import time
import csv

#Busca de profundidade com grafos direcionados Usando representação da lista de adjacência
class Graph:
    # Construtor
    def __init__(self):
        # dicionário default para armazenar o gráfico
        self.graph = defaultdict(list)
 
    # Função para adicionar uma aresta ao gráfico
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    # função recursiva  de DFS
    def DFSUtil(self, v, visited):
        # Marca o nó atual como visitado e imprime
        visited.add(v)
        print(v,end=" ")
 
        # recorrente para todos os vértices adjacentes a este vértice
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    # A função para fazer a travessia DFS. Ele usa DFSUtil recursivo
    def DFS(self, v):
        # cria um conjunto para armazenar todos os vértices visitados
        visited = set()
        # chama a função auxiliar recursiva para imprimir a travessia DFS a partir de todos vértices um por um
        self.DFSUtil(v, visited)

#Le o grafo
with open ('Grafo.CSV', mode='r') as csv_file:
    dados_csv = csv.reader(csv_file, delimiter = ';')
    k = 0
    Vertice = []
    g = Graph()
    for k, linha in enumerate(dados_csv):
        for i, coluna in enumerate(linha):
            if k == 0:
                Vertice.append(coluna)
            elif coluna == '1':
                g.addEdge(Vertice[k-1], Vertice[i])


# cria um grafo direcionado
"""
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 5)
g.addEdge(1, 0)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(3, 1)
g.addEdge(3, 5)
g.addEdge(3, 4)
g.addEdge(4, 3)
g.addEdge(5, 0)
g.addEdge(5, 3)
g.addEdge(3, 6)
g.addEdge(2, 7)
g.addEdge(6, 7)
g.addEdge(7, 6)
"""

inicio = time.time()
g.DFS('2')
fim = time.time()

#Exibe tempo decorrido
print("\nTempo pecorrido: {0}".format(fim-inicio))
