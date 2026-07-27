# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:13:30 2026

@author: Joaco
"""
import numpy as np
# def magiCuadrados(n, i, j):
    
#     for k in range (1, n+1, 1):
#         for q in range (j, n, 1):
#             if not(esta(res, k)):
#                 res[i][q] = k
#                 return magiCuadrados(n, i, j+1)
#         if i > 1:
#             if sumaFila(res, i) != sumaFila(res, i-1):
#                 return -1
    
#     i += 1
#     if i==n:
#         for k in range(0, n-1, 1):
#             if sumaColumna(res, i) != sumaColumna(res, i+1):
#                 return -1
        
#         if not(sumaDiagonalesIguales(res)):
#             return -1
        
#     return magiCuadrados(n, i+1, 0)

#%% PUNTO 2B: FUNCIONES AUXILIARES
def esta(numerosUsados, k):
    # k-1 porque los números van de 1 a n^2, pero los índices de 0 a n^2 - 1
    return numerosUsados[k-1]

def sumaFila(res, i):
    suma = 0
    for j in range(len(res)):
        suma += res[i][j]
    return suma

def sumaColumna(res, j):
    suma = 0
    n = len(res)
    for i in range(n):
        suma += res[i][j]
    return suma

def sumaDiagonalesIguales(res, numeroMagico):
    n = len(res)
    sumaPrincipal = 0
    sumaSecundaria = 0
    
    for k in range(n):
        # Diagonal principal: (0,0), (1,1), (2,2)...
        sumaPrincipal += res[k][k]
        # Diagonal secundaria: (0, n-1), (1, n-2), (2, n-3)...
        sumaSecundaria += res[k][n - 1 - k]
        
    # Retorna True solo si ambas cumplen la condición de ser "mágicas"
    return sumaPrincipal == numeroMagico and sumaSecundaria == numeroMagico

#%% PUNTO 2B: FUNCIÓN PRINCIPAL
def magiCuadrados(n, i, j, res, numerosUsados, numeroMagico):
    if i==n:
        for k in range(0, n, 1):
            if sumaColumna(res, k) != numeroMagico:
                return 0
        
        if sumaDiagonalesIguales(res, numeroMagico):
            return 1
        else:
            return 0
    
    contador = 0
    for k in range(1, n**2 +1, 1):
        if not(esta(numerosUsados, k)):
            res[i][j] = k
            numerosUsados[k-1] = True
            if j == n -1:
                if i == 0:
                    numeroMagicoPrimerFila = sumaFila(res, 0)
                    contador += magiCuadrados(n, i+1, 0, res, numerosUsados, numeroMagicoPrimerFila)
                elif sumaFila(res, i) == numeroMagico:
                    contador += magiCuadrados(n, i+1, 0, res, numerosUsados, numeroMagico)
            else:
                contador += magiCuadrados(n, i, j+1, res, numerosUsados, numeroMagico)
                
            numerosUsados[k-1] = False
    return contador
                

# Inicialización
n = 3
matriz = [[0 for _ in range(n)] for _ in range(n)]
usados = [False] * (n**2)

# Llamada
total = magiCuadrados(n, 0, 0, matriz, usados, 0)

print(f"Para n={n}, se encontraron {total} cuadrados mágicos.")
# Debería imprimir: Para n=3, se encontraron 8 cuadrados mágicos.


#%% PUNTO 2D
def magiCuadradosV2(n, i, j, res, numerosUsados, numeroMagico, sumaParcialFila, sumasColumnas):
    if i==n:
        for k in range(0, n, 1):
            if sumasColumnas[k] != numeroMagico:
                return 0
        
        if sumaDiagonalesIguales(res, numeroMagico):
            return 1
        else:
            return 0
    
    contador = 0
    for k in range(1, n**2 +1, 1):
        if not(esta(numerosUsados, k)) and sumaParcialFila + k <= numeroMagico and sumasColumnas[j] + k <= numeroMagico:
            res[i][j] = k
            sumaParcialFila += k
            sumasColumnas[j] += k
            numerosUsados[k-1] = True
            if j == n -1:
                if i == 0:
                    numeroMagicoPrimerFila = sumaFila(res, 0)
                    contador += magiCuadradosV2(n, i+1, 0, res, numerosUsados, numeroMagicoPrimerFila, 0, sumasColumnas)
                elif sumaParcialFila == numeroMagico:
                    contador += magiCuadradosV2(n, i+1, 0, res, numerosUsados, numeroMagico, 0, sumasColumnas)
            else:
                contador += magiCuadradosV2(n, i, j+1, res, numerosUsados, numeroMagico, sumaParcialFila, sumasColumnas)
                
            numerosUsados[k-1] = False
            sumaParcialFila -= k
            sumasColumnas[j] -= k
    return contador
                
                
#numeroMagicoInicial = (n^2 + 1)*(n^2)/2 - (n^2 - n)(n^2 - n - 1)/2
                
#%% PUNTO 2E
def magiCuadradosV3(n, i, j, res, numerosUsados, numeroMagico, sumaParcialFila, sumasColumnas):
    if i==n:
        for k in range(0, n, 1):
            if sumasColumnas[k] != numeroMagico:
                return 0
        
        if sumaDiagonalesIguales(res, numeroMagico):
            return 1
        else:
            return 0
    
    contador = 0
    for k in range(1, n**2 +1, 1):
        if not(esta(numerosUsados, k)) and sumaParcialFila + k <= numeroMagico and sumasColumnas[j] + k <= numeroMagico:
            res[i][j] = k
            sumaParcialFila += k
            sumasColumnas[j] += k
            numerosUsados[k-1] = True
            if j == n -1:
                if sumaParcialFila == numeroMagico:
                    contador += magiCuadradosV3(n, i+1, 0, res, numerosUsados, numeroMagico, 0, sumasColumnas)
            else:
                contador += magiCuadradosV3(n, i, j+1, res, numerosUsados, numeroMagico, sumaParcialFila, sumasColumnas)
                
            numerosUsados[k-1] = False
            sumaParcialFila -= k
            sumasColumnas[j] -= k
    return contador
                                
#numeroMagico = (n***3 +n)/2


#%% PUNTO 3a sin return

def maxiSubconjunto(M, k, indice, subconjunto, sumaParcial, subconjuntoMaximo, sumaMaxima):
    if len(subconjunto)<k:
        if len(subconjunto) + (n - indice) < k: 
            return
        for i in range(indice, len(M), 1):
            subconjunto.append(i)
            aux = 0
            for j in subconjunto:
                if j != i :
                    aux += 2*M[j][i]
                else:
                    aux += M[j][j]
            subconj = maxiSubconjunto(M, k, i+1, subconjunto, sumaParcial + aux, subconjuntoMaximo, sumaMaxima)
            subconjunto.pop()
    else:
        if sumaParcial > sumaMaxima[0]:
            subconjuntoMaximo.clear()
            subconjuntoMaximo.append(subconjunto.copy())
            sumaMaxima[0] = sumaParcial
        elif sumaParcial == sumaMaxima[0]:
            subconjuntoMaximo.append(subconjunto.copy())
   
#%%
# Datos de entrada
M = [
    [0, 10, 10, 1],
    [10, 0, 5, 2],
    [10, 5, 0, 1],
    [1, 2, 1, 0]
]
k = 3
n = 4

# Inicialización de variables de "Estado Global"
soluciones = []
# Usamos una lista de un elemento para que sea mutable y pase por referencia
record = [0]

# Llamada inicial
maxiSubconjunto(M, k, 0, [], 0, soluciones, record)

print(f"Suma Máxima encontrada: {record[0]}")
print(f"Subconjuntos óptimos: {soluciones}")

    # if suma > sumaMaxima:
    #     sumaMaxima = suma
    #     subconjuntoMaximo = subconj
    
    # return subconjuntoMaximo
        
#%% PUNTO 3A con return
def maxiSubconjuntoV2(M, k, indice, subconjunto, sumaParcial):
    
    n = len(M)
    
    if len(subconjunto) == k: #caso subconjunto de k elementos. Etapa soluciones candidatas
        return [(subconjunto.copy(), sumaParcial)]
    
    #En primera instancia, una regla de factibilidad: si no alcanzo a completar k elementos con los indices que quedan, descarto
    if len(subconjunto) + (n - indice) < k:
        return []
    
    
    #Vemos primero cuando al subconjunto le falta algún(os) índice(s)
    soluciones_candidatas = [] 
    #Para no caer en repeticiones del estilo {1,2} {2,1}, siempre buscaré insertar elementos mayores
        
    #Etapa soluciones parciales
    #Creo diversos subconjuntos a partir del índice que describe "el menor elemento mayor" que se podría incorporar al conjunto.
    for i in range(indice, n, 1):
        #Agrego el índice i a mi subconjunto de índices
        subconjunto.append(i)
        #Creo un auxiliar para después borrar lo que ese índice i le sumo a un subconjunto, con el fin de poder usar la variable SumaParcial
        aux_suma = 0
        #Sumo entonces lo que "agrega" la variable i
        for j in subconjunto:
            if j != i :
                #Notar que la matriz es simétrica, luego Mij = Mji
                aux_suma += 2*M[j][i]
            else: #caso i=j se suma una sola vez
                aux_suma += M[j][j]
        #Continúo formando el subconjunto, pero esta vez el índice es i+1
        soluciones_parciales = maxiSubconjuntoV2(M, k, i+1, subconjunto, sumaParcial + aux_suma)
        #Quito luego el índice agregado, y resto la suma adicionada, con el fin de ser usado para el resto del bucle
        soluciones_candidatas.extend(soluciones_parciales)
        subconjunto.pop()
    
    #si no consigo nuevas soluciones candidatas, devuelvo vacío
    if len(soluciones_candidatas) == 0:
        return []
    
    #Momento de seleccionar las soluciones válidas
    subconjuntoMaximo = []
    sumaMaxima = -1
    
    for tupla in soluciones_candidatas:
        solucion_candidata = tupla[0]
        suma_candidata = tupla[1]
        if suma_candidata > sumaMaxima: #Si superé mi máximo, entonces es la nueva y única solución válida
            sumaMaxima = suma_candidata
            subconjuntoMaximo.clear()
            subconjuntoMaximo.append((solucion_candidata.copy(), sumaMaxima))
        elif suma_candidata == sumaMaxima: #si igualé el máximo, entonces es otra solución válida
            subconjuntoMaximo.append((solucion_candidata.copy(), sumaMaxima))
        
    return subconjuntoMaximo


#%%
# Datos de entrada
M2 = [
    [0, 10,  1, 10],  # Nodo 0
    [10, 0, 10,  1],  # Nodo 1
    [1, 10,  0, 10],  # Nodo 2
    [10, 1, 10,  0]   # Nodo 3
]

# Llamada inicial
# Llamada inicial
resultado_con_sumas = maxiSubconjuntoV2(M2, 2, 0, [], 0)

# Limpieza manual (solo subconjuntos)
solo_subconjuntos = []
for res in resultado_con_sumas:
    solo_subconjuntos.append(res[0])

print(solo_subconjuntos)

resultado_con_sumas = maxiSubconjuntoV2(M, k, 0, [], 0)

# Limpieza manual (solo subconjuntos)
solo_subconjuntos = []
for res in resultado_con_sumas:
    solo_subconjuntos.append(res[0])

print(solo_subconjuntos)


#%% PUNTO 4

def rutaMinima(D, permutacionActual, sumaActual, indicesUsados, permutacionMinima, sumaMinima):
    n = len(D)
    tamañoPermutacion = len(permutacionActual)
    
    #Soluciones candidatas
    if tamañoPermutacion == n:
        #Para ser una solución óptima, debe haber superado la sumaMinima actual (si la iguala, me quedo con la que ya tenía)
        if sumaMinima[0] > sumaActual:
            sumaMinima[0] = sumaActual
            permutacionMinima.clear()
            permutacionMinima.append(permutacionActual.copy())
        else:
            return
    
    if sumaActual > sumaMinima[0]: #Poda por optimalidad: si ya superé la sumaMinima, no avanzo más en esta rama
        return
    
    for i in range(0, n, 1): #Soluciones parciales. Las extiendo agregando las diferentes posibilidades de índices restantes, formando cada subconjunto posible
        if indicesUsados[i] == False: #Debo asegurarme de que el índice a agregar no haya sido usado
            indicesUsados[i] = True #en caso de que así sea, lo agrego y actualizo los indices usados
            if tamañoPermutacion == n - 1: #debo sumar adicionalmente la vuelta
                permutacionActual.append(i)
                rutaMinima(D, permutacionActual, sumaActual + D[permutacionActual[tamañoPermutacion - 1]][i] + D[i][permutacionActual[0]], indicesUsados, permutacionMinima, sumaMinima)
            elif tamañoPermutacion == 0: #solo agrego
                permutacionActual.append(i)
                rutaMinima(D, permutacionActual, sumaActual, indicesUsados, permutacionMinima, sumaMinima)
            else: #debo sumar el pasaje de un índice al siguiente
                auxSuma = D[permutacionActual[tamañoPermutacion - 1]][i]
                permutacionActual.append(i)
                rutaMinima(D, permutacionActual, sumaActual + auxSuma, indicesUsados, permutacionMinima, sumaMinima)
            indicesUsados[i] = False #para poder seguir el bucle, revierto el estado original
            permutacionActual.pop()
            
        
        
#%%  
D = [ [0,1,10,10],
     [10, 0, 3 ,15],
     [21, 17, 0, 2],
     [2, 22, 30, 0]
     ]        

indicesUsados = [False, False, False, False]
permutacionMinima = []
sumaMinima = [float('inf')]
rutaMinima (D, [], 0, indicesUsados, permutacionMinima, sumaMinima)

#%%
# Matriz D de 4x4
D2 = [
    [0, 10, 15, 20],
    [5,  0,  9, 10],
    [6, 13,  0, 12],
    [8,  8,  9,  0]
]

# Una permutación candidata pi* (usando índices 0, 1, 2, 3)
# Esto representa el camino: 0 -> 2 -> 3 -> 1 -> (vuelve a 0)

permutacionMinima2 = []
indicesUsados2 = [False, False, False, False]
sumaMinima2 = [float('inf')]
rutaMinima(D2, [], 0,indicesUsados, permutacionMinima2, sumaMinima2)


#%% Punto 5

def palabra(palabra):
    return True

def palabrasEnCadena(cadena, posicionInicial, posicionFinal):
    n = len(cadena)
    if posicionFinal == n-1:
        return (palabra(cadena, posicionInicial, posicionFinal) and palabra(cadena, n-1, n)) or palabra(cadena, posicionInicial, n)
    
    else:
        return (palabra(cadena, posicionInicial, posicionFinal) and palabrasEnCadena(cadena, posicionFinal, posicionFinal + 1)) or (palabrasEnCadena(cadena, posicionInicial, posicionFinal +1)) 


#suponiendo palabra toma las letras correspondiente desde la posicionInicial (incluyendo) hasta posicionFinal (excluyendo)

#%% Punto 7: función dobra no recursiva, complejidad O(n), sin considerar guiones

def dobra(cadena):
    n = len(cadena)
    i = 0
    sumaVocalesSeguidas = 0
    sumaConsonantesSeguidas = 0
    esCorrecta = True
    huboE = False
    while esCorrecta and i < n:
        if cadena[i] in {'a', 'e', 'i', 'o', 'u'}:
            sumaVocalesSeguidas += 1
            sumaConsonantesSeguidas = 0
            if cadena[i] == 'e':
                huboE = True
            if sumaVocalesSeguidas == 3:
                return False
        else:
            sumaConsonantesSeguidas += 1
            sumaVocalesSeguidas = 0
            if sumaConsonantesSeguidas == 3:
                return False
    
    return huboE
        


#%% Punto 8

def cadenasDeAdicion(n, cadenaActual, tamanioActual, cadenaMinima, tamanioMinimo, indice):
    # Caso base: Ya decidimos sobre todos los números entre 1 y n
    if indice == n:
        # 1. Extraemos los números que marcamos como True
        elementos = [i + 1 for i in range(n) if cadenaActual[i]]
        
        # 2. Validamos si es una cadena de adición
        esValida = True
        # El primer elemento (1) no se valida. Empezamos del segundo.
        for idx in range(1, len(elementos)):
            valor = elementos[idx]
            sePuedeFormar = False
            # ¿Existen dos previos (pueden ser el mismo) que sumen 'valor'?
            for a in range(idx):
                for b in range(idx):
                    if elementos[a] + elementos[b] == valor:
                        sePuedeFormar = True
                        break
                if sePuedeFormar: break
            
            if not sePuedeFormar:
                esValida = False
                break
        
        # 3. Si es válida y es más corta que la que teníamos, la guardamos
        if esValida and tamanioActual < tamanioMinimo[0]:
            tamanioMinimo[0] = tamanioActual
            cadenaMinima.clear()
            cadenaMinima.extend(elementos)
        return

    # --- BACKTRACKING (Decisión por cada número) ---
    
    # Si el número es 1 o n, ya sabemos que TIENEN que estar (True)
    if indice == 0 or indice == n - 1:
        cadenaActual[indice] = True
        cadenasDeAdicion(n, cadenaActual, tamanioActual + 1, cadenaMinima, tamanioMinimo, indice + 1)
    else:
        # Opción A: Incluir el número (indice + 1)
        if tamanioActual + 1 < tamanioMinimo[0]: # Poda simple
            cadenaActual[indice] = True
            cadenasDeAdicion(n, cadenaActual, tamanioActual + 1, cadenaMinima, tamanioMinimo, indice + 1)
        
        # Opción B: NO incluir el número
        cadenaActual[indice] = False
        cadenasDeAdicion(n, cadenaActual, tamanioActual, cadenaMinima, tamanioMinimo, indice + 1)

#%%
# --- Ejemplo de uso ---
n_target = 20
conjuntoMinimo = []
min_tam = [99] # Usamos lista para que sea mutable (paso por referencia)

# Inicializamos con False para todos los números del 1 al n
cadenasDeAdicion(n_target, [False] * n_target, 0, conjuntoMinimo, min_tam, 0)

print(f"Cadena mínima para {n_target}: {conjuntoMinimo}")











