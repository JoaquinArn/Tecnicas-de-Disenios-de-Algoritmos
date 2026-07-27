# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:35:04 2026

@author: ASUS
"""

#%% Punto 27: suma selectiva en O(n log n)

# Primero usaremos merge_sort para ordenar X
# El algoritmo lo obtuve de asimov.cloud

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1️⃣ División
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2️⃣ Fusión
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    # Añadir los restos (solo uno de los dos bucles se ejecutará)
    merged.extend(right[j:])
    merged.extend(left[i:])
    return merged

def sumaSelectiva(X, k):
    X_ordenada = merge_sort(X)
    S = X_ordenada[:k]
    valor_maximo = sum(X_ordenada[i] for i in range(k))
    
    return valor_maximo, S

print(sumaSelectiva([4,2,7,9,100,1], 3))


#%% Punto 27: suma selectiva en O(n log k)

def k_mas_grandes(X, k):
    res = []
    for i in range(len(X)):
        if i < k-1:
            res.append(X[i])
        
        if i == k -1:
            res.append(X[i])
            build_heap(res)
        
        if i>= k:
            if res:
                res = min_heap(res, X[i])
    
    return res

def build_heap(arr):
    k = len(arr)
    i = k // 2 - 1
    while i > -1:
        heapify(arr, i)
        i -= 1
    
        

def min_heap(res, e):
    if res[0] < e:
        res[0] = e
        heapify(res, 0)
    
    return res
        
def heapify(arr, i):
    k =len(arr)
    smallest = i          # Inicializa el mayor como raíz
    left = 2 * i + 1     # hijo izquierdo
    right = 2 * i + 2    # hijo derecho
    
    if left < k and arr[left] < arr[smallest]:
        smallest = left

    if right < k and arr[right] < arr[smallest]:
        smallest = right
    # # Si el hijo derecho es menor que el menor actual
    # if right < k and arr[right] < arr[smallest]:
    #     smallest = right
        
    # # Si el hijo izquierdo es menor que la raíz
    # if left < k and arr[left] < arr[smallest]:
    #     smallest = left


    # Si el menor no es la raíz, intercambiamos y continuamos heapificando
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest)
        
    
    

def sumaSelectiva(X,k):
    k_mayores = k_mas_grandes(X,k) 
    X_ordenada = merge_sort(k_mayores)
    S = X_ordenada[:k]
    valor_maximo = sum(X_ordenada[i] for i in range(k))
    
    return valor_maximo, S

print(sumaSelectiva([1000, 4,2,7,9,100,1], 3))


#%% Punto 28: SumaGolosa

def extraer_minimo(X):
    minimo = X[0]
    X[0] = X[len(X)-1]
    X.pop()
    heapify(X, 0)
    return minimo

def heapifyUp(X, i):
    if i>0:
        padre = (i-1)//2
        if X[padre] > X[i]:
            e = X[padre]
            X[padre] = X[i]
            X[i] = e
            heapifyUp(X, padre)
    
    
def agregar_elemento(X, e):
    X.append(e)
    heapifyUp(X, len(X) -1)

def suma_golosa(X):
    X_ord = X.copy()
    build_heap(X_ord)
    
    costo = 0
    k = len(X_ord)
    
    while k != 1:
        elem_mas_chico = extraer_minimo(X_ord)
        seg_elem_mas_chico = extraer_minimo(X_ord)
        suma = elem_mas_chico + seg_elem_mas_chico
        costo += suma
        agregar_elemento(X_ord, suma)
        k = len(X_ord)
        
    return costo


#%% Punto 32: division pandémica

def division_pandemica(E, C):
    A = []
    B = []
    
    for i in range(len(E)):
        cantidad_cercanos_A = 0
        cantidad_cercanos_B = 0
        for k in range(len(C)):
            (r,s) = C[k]
            if i==r:
                if s in A:
                    cantidad_cercanos_A +=1
                elif s in B:
                    cantidad_cercanos_B +=1
            
            if i==s:
                if r in A:
                    cantidad_cercanos_A +=1
                elif r in B:
                    cantidad_cercanos_B +=1
                    
        if cantidad_cercanos_A <= cantidad_cercanos_B:
            A.append(i)
        else:
            B.append(i)
    
    return A,B
    
print(division_pandemica([0,1,2,3], [(0,1), (1,2), (2,3)]))

#%% Punto 32: versión pandémica, otra versión

def division_pandemica(E, C):
    A = [False for _ in range(len(E))]
    B = [False for _ in range(len(E))]
    
    pares_cercanos = {}
    for (i,j) in C:
        if i in pares_cercanos:
            pares_cercanos[i].append(j)
        
        elif i not in pares_cercanos:
            pares_cercanos[i] = [j]
            
        if j in pares_cercanos:
            pares_cercanos[j].append(i)
        
        elif j not in pares_cercanos:
            pares_cercanos[j] = [i]
        
    for i in range(len(E)):
        cantidad_cercanos_A = 0
        cantidad_cercanos_B = 0
        cercanos_a_i = pares_cercanos.get(i, [])
        for estudiante in cercanos_a_i:
            if A[estudiante]:
                cantidad_cercanos_A += 1
            if B[estudiante]:
                cantidad_cercanos_B +=1
                    
        if cantidad_cercanos_A <= cantidad_cercanos_B:
            A[i] = True
            
        else:
            B[i] = True
    
    A = [i for i, val in enumerate(A) if val]
    B = [i for i, val in enumerate(B) if val]

    
    return A,B
    

print(division_pandemica([0,1,2,3], [(0,1), (1,2), (2,3)]))


#%% Punto 33: maxmex

def maxmex(X):
    elementos = {}
    repetidos = []
    for elemento in X:
        if elementos.get(elemento, 0) != 0:
            elementos[elemento] += 1
        
        else:
            elementos[elemento] = 1
    
    buscado = 0
    n = len(X)
    maximo_alcanzado = 0
    i = 0
    
    while buscado < n:
        if elementos.get(buscado, 0) != 0:
            buscado +=1
        else:
            maximo_alcanzado = buscado
            buscado = n+1
            
    for elemento in elementos:
         if elemento < maximo_alcanzado:
             repetidos.extend(elemento for j in range(elementos[elemento] - 1))
         else:
             repetidos.extend(elemento for j in range(0, elementos[elemento]))
    
    m = n - len(repetidos)
    suma = maximo_alcanzado*(maximo_alcanzado + 1)/2 + (n - m)*maximo_alcanzado
    
    permutacion = [i for i in range(maximo_alcanzado)]
    permutacion.extend(repetidos)
    
    return permutacion, suma

print(maxmex([0,0,1,1, 3, 3,4]))
    

#%% Punto 33: maxmex

def maxmex(X):
    n = len(X)
    elementos = [0 for _ in range(n)]
    saltos = []
    for elemento in X:
        if elemento < n and elementos[elemento] != 0:
            elementos[elemento] += 1
        elif elemento < n:
            elementos[elemento] = 1
        else:
            saltos.append(elemento)
    
    buscado = 0
    maximo_alcanzado = 0
    i = 0
    
    while buscado < n:
        if elementos[buscado] != 0:
            saltos.extend([buscado] * (elementos[buscado] - 1))
            buscado +=1
        else:
            maximo_alcanzado = buscado
            for i in range(maximo_alcanzado, n):
                saltos.extend([i] * elementos[i])
            buscado = n+1
    
    
    m = n - len(saltos)
    suma = maximo_alcanzado*(maximo_alcanzado + 1)/2 + (n - m)*maximo_alcanzado
    
    permutacion = [i for i in range(maximo_alcanzado)]
    permutacion.extend(saltos)
    
    return permutacion, suma

print(maxmex([0,0,1,1, 3, 3,4]))




























