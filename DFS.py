from collections import defaultdict
 

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


# cria um grafo direcionado
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)
