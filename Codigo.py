grafo = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'c', 'e'],
    'c': ['b', 'e'],
    'd': ['a', 'e'],
    'e': ['a', 'b', 'c', 'd', 'f'],
    'f': ['e']
}

def busca_em_largura(grafo, vertice_do_grafo):
    fila = []
    largura = {}
    l = 1 
    pai = {} 
    nivel = {} 
    aresta = {} 

    
    fila.append(vertice_do_grafo)
    largura[vertice_do_grafo] = l 
    pai[vertice_do_grafo] = None 
    nivel[vertice_do_grafo] = 1 

    
    while len(fila):
        vertice = fila.pop(0) 
        
        for vizinho in grafo.get(vertice):
            
            if not largura.get(vizinho): 
                fila.append(vizinho) 
                l += 1 
                largura[vizinho] = l
                pai[vizinho] = vertice
                nivel[vizinho] = nivel[vertice] + 1 
            
            print('%s -> %s:' % (str(vertice), str(vizinho)))
            if pai[vizinho] == vertice or pai[vertice] == vizinho:
                aresta[(vertice, vizinho)] = 'aresta de arvore'
                print('aresta de arvore')
            elif nivel[vertice] == nivel[vizinho]:
                if pai[vertice] == pai[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta irma'
                    print('aresta irma')
                else:
                    aresta[(vertice, vizinho)] = 'aresta primo'
                    print('aresta primo')
            else:
                if nivel[vertice] < nivel[vizinho]:
                    aresta[(vertice, vizinho)] = 'aresta tia'
                    print('aresta tia')
                else:
                    aresta[(vertice, vizinho)] = 'aresta sobrinha'
                    print('aresta sobrinha')

    return largura, pai, aresta, nivel

largura, pai, aresta, nivel = busca_em_largura(grafo, 'a')
