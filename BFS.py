from collections import defaultdict
import time
import csv

#Busca em largura com grafos direcionados Usando representação da lista de adjacência
class Graph:
 
    # Construtor
    def __init__(self):
 
        # dicionário default para armazenar o gráfo
        self.graph = defaultdict(list)
 
    # Função para adicionar aresta ao gráfo
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Função para dar print o BFS do grafo
    def BFS(self, s):
 
        # Marca todos os vértices como não visitados
        visited = [False] * (max(self.graph) + 1)
        
        # Cria uma fila para BFS
        queue = []
 
        # Marca o nó de origem como visitado e efileirado
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            #Desenfileira um vértice e imprime
            s = queue.pop(0)
            print (s, end = " ")
 
            # Obtém todos os vértices adjacentes do
            # vértice s desenfileirado. Se um adjacente
            # não foi visitado, então marque-o
            # visitado e enfileirado
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

#Le o grafo
with open ('Grafo.CSV', mode='r') as csv_file:
    dados_csv = csv.reader(csv_file, delimiter = ';')
    k = 0
    Vertice = []
    g = Graph()
    for k, linha in enumerate(dados_csv):
        for i, coluna in enumerate(linha):
            if k == 0:
                Vertice.append(int(coluna))
            elif coluna == '1':
                g.addEdge(Vertice[k-1], Vertice[i])


"""
# cria um grafo direcionado
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
g.BFS(2)
fim = time.time()
 
#Exibe tempo decorrido
print("\nTempo pecorrido: {0}".format(fim-inicio))
