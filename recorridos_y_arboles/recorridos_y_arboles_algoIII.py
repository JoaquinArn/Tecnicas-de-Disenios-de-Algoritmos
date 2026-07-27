# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:52:49 2026

@author: ASUS
"""
from collections import deque

#%% Ejercicio 1c

def recorrer(G):
    #Devuelvo las variables pred y distancias_a_raiz
    #pred[i] = padre de i
    #distancias_a_raiz[i] = d(r,i) donde r = raiz = 0
    r = 0
    pred = [0 for _ in range(len(G))]
    distancias_a_raiz = [-1 for _ in range(len(G))]
    distancias_a_raiz[r] = 0
    
    #Algoritmo DFS
    pila = deque()
    pila.append(r)
    while len(pila) != 0:
        i = pila[-1]
        hay_vecino_no_visitado = False
        for j in G[i]:
            if distancias_a_raiz[j] == -1:
                pred[j] = i
                distancias_a_raiz[j] = distancias_a_raiz[i] + 1
                pila.append(j)
                hay_vecino_no_visitado = True
                break
            
        if not hay_vecino_no_visitado:
            pila.pop()
            
    return pred, distancias_a_raiz
    

def esBipartito(G):
    #Si el grafo G es bipartito, devuelvo una bipartición V,W
    #Caso contrario, devuelvo un ciclo C
    
    #Utilizando DFS, consigo las variables pred y distancias_a_raiz
    #pred[i] = padre de i
    #distancias_a_raiz(i) = d(r,i) donde r = raiz = 0
    pred, distancias_a_raiz = recorrer(G)
    
    #Defino el vector D donde D[i] = 0 si d(r,i) es par; y 1 en caso contrario
    D = [0 for _ in range(len(G))]

    for i in range(len(G)):
        if distancias_a_raiz[i] % 2 != 0:
            D[i] = 1
    
    
    #Recorro E(G)
    for i in range(len(G)):        
        #Mi intención es, si no se encuentra un arco (i,j) con D[i] = D[j], devolver V y W
        #Caso contrario, devuelvo un ciclo 
        for j in G[i]:
            if D[i] != D[j]:
                continue
            
            else: #Grafo no bipartito, pues hallé arco entre vértices de misma paridad en su distancia a r
                v = i
                w = j
                #Debo identificar cuál de los dos es un ancestro del otro
                #Para ello, observo sus distancias a con la raíz.
                #El vértice de menor distancia a con la raíz, es el ancestro.
                #En ambos casos, defino C el ciclo (conjunto de aristas)
                C = list()
                
                if distancias_a_raiz[v] <= distancias_a_raiz[w]: #caso v es el ancestro
                    actual = w
                    while actual != v:
                        C.append((actual, pred[actual]))
                        actual = pred[actual]
                    
                    C.append((v,w))
                    return C
                
                else: #caso w es el ancestro
                    actual = v
                    while actual != w:
                        C.append((actual, pred[actual]))
                        actual = pred[actual]
                    
                    C.append((w, v))
                    return C
            
    #¡El grafo es bipartito!
    
    V = [i for i in range(len(D)) if D[i] == 0]
    W = [i for i in range(len(D)) if D[i] == 1]
    return V, W

    
#%% Ejercicio 1d

def recorrer(G, r, pred, distancias_a_raiz):
    #Devuelvo las variables pred y distancias_a_raiz
    #pred[i] = padre de i
    #distancias_a_raiz[i] = d(r,i) donde r = raiz = 0
    distancias_a_raiz[r] = 0
    
    #Algoritmo DFS
    pila = deque()
    pila.append(r)
    while len(pila) != 0:
        i = pila[-1]
        hay_vecino_no_visitado = False
        for j in G[i]:
            if distancias_a_raiz[j] == -1:
                pred[j] = i
                distancias_a_raiz[j] = distancias_a_raiz[i] + 1
                pila.append(j)
                hay_vecino_no_visitado = True
                break
            
        if not hay_vecino_no_visitado:
            pila.pop()
            
    

def esBipartito(G):
    #Si el grafo G es bipartito, devuelvo una bipartición V,W
    #Caso contrario, devuelvo un ciclo C
    
    #Utilizando DFS, consigo las variables pred y distancias_a_raiz
    #pred[i] = padre de i
    #distancias_a_raiz(i) = d(r,i) donde r = raiz 
    
    #Defino el vector D donde D[i] = 0 si d(r,i) es par; y 1 en caso contrario
    D = [0 for i in range(len(G))]
    r = 0
    pred = [0 for _ in range(len(G))]
    distancias_a_raiz = [-1 for _ in range(len(G))]
    
    #Analizo cada componente conexa
    for r in range (len(G)):
        if distancias_a_raiz[r] == -1:
            recorrer(G, r, pred, distancias_a_raiz)
        
    
    #Una vez recorrido cada vértice, defino las paridades
    for i in range(len(G)):
        if distancias_a_raiz[i] % 2 != 0:
            D[i] = 1
        
    #Recorro E(G)
    for i in range(len(G)):        
        #Mi intención es, si no se encuentra un arco (i,j) con D[i] = D[j], devolver V y W
        #Caso contrario, devuelvo un ciclo 
        for j in G[i]:
            if D[i] != D[j]:
                continue
                    
            else: #Grafo no bipartito, pues hallé arco entre vértices de misma paridad en su distancia a r
                v = i
                w = j
                #Debo identificar cuál de los dos es un ancestro del otro
                #Para ello, observo sus distancias a con la raíz.
                #El vértice de menor distancia a con la raíz, es el ancestro.
                #En ambos casos, defino C el ciclo (conjunto de aristas)
                C = list()
                            
                if distancias_a_raiz[v] <= distancias_a_raiz[w]: #caso v es el ancestro
                    actual = w
                    while actual != v:
                        C.append((actual, pred[actual]))
                        actual = pred[actual]
                                
                    C.append((v,w))
                    return C
                            
                else: #caso w es el ancestro
                    actual = v
                    while actual != w:
                        C.append((actual, pred[actual]))
                        actual = pred[actual]
                                
                    C.append((w, v))
                    return C
                        
    #¡El grafo es bipartito!
    
    V = [i for i in range(len(D)) if D[i] == 0]
    W = [i for i in range(len(D)) if D[i] == 1]
    return V, W
    
#%% Ejercicio 8

def distancia_minima(M, x, y, k, w):
    #Devuelvo la cantidad mínima de pasos que debo hacer desde (x,y) para obtener w
    
    if w >= k: #pues M[x][y] < k para todo x,y; y al desplazarme, el módulo de las sumas devuelve un número menor a k
        return 'no hay solucion posible'
    
    #veamos además si no es necesario realizar movimientos:
    if M[x][y] == w:
        return 0
    
    #Primero formemos G
    #La estructuro como una matriz del mismo tamaño que M donde cada posicion G[x][y] es una lista que denota los movimientos posibles a partir de (x,y)
    m = len(M)
    n = len(M[0])
    
    G = [[list() for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i > 0: #¿puedo subir?
                G[i][j].append((i-1, j))
            if i < m-1: #¿puedo bajar?
                G[i][j].append((i+1, j))
            if j > 0: #¿puedo ir a la izquierda?
                G[i][j].append((i, j-1))
            if j < n-1: #¿puedo ir a la derecha?
                G[i][j].append((i, j+1))
    
    
    descubierto = [[[False for _ in range(n)] for _ in range(m)] for _ in range(k)]
    distancias_a_raiz = [[[-1 for _ in range(n)] for _ in range(m)] for _ in range(k)]
    distancias_a_raiz[M[x][y]][x][y] = 0
    descubierto[M[x][y]][x][y] = True
    
    #Algoritmo BFS
    cola = deque()
    cola.append((M[x][y], x, y))
    while len(cola) != 0: #mientras haya estados/movimientos no analizados
        (v,x_actual,y_actual) = cola.popleft()
        for (x_prima, y_prima) in G[x_actual][y_actual]: #veo los espacios adyacentes
            v_prima = (v + M[x_prima][y_prima]) % k
            if descubierto[v_prima][x_prima][y_prima] == False: #si el estado no fue ya alcanzado, entonces debo procesarlo
                distancias_a_raiz[v_prima][x_prima][y_prima] = distancias_a_raiz[v][x_actual][y_actual] + 1
                descubierto[v_prima][x_prima][y_prima] = True
                
                if v_prima == w: #si alcancé ya la suma, entonces por la forma del recorrido, estamos en la distancia mínima
                    return distancias_a_raiz[v_prima][x_prima][y_prima]
                else: #si no alcancé la suma, lo agrego a la cola para más tarde revisar si es posible alcanzar w habiendome desplazado en esta dirección
                    cola.append((v_prima, x_prima, y_prima))
            
    #Si llegué hasta acá es porque no fue posible un recorrido que me de w
    return 'no hay solucion posible'
    





    