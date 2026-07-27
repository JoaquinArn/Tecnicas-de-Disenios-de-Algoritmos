# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 08:48:45 2026

@author: ASUS
"""

import math
import numpy as np

#%% Punto 9
def kingArmy(di):
    
    #Si el valor solicitado ya está cargado en mi estructura de memoizacion, lo retorno
    if memoria[di] != -1:
        return memoria[di]
    
    #Si estoy en casos base 0 y 1, debo guardarlos en mi estructura de memoizacion para que siempre caiga en la anterir cláusula
    #Esto ocurre solo una vez
    if di == 0 or di == 1:
        memoria[di] = 1
        return 1
    
    #Caso recursivo: busco las cantidades de los días anteriores y las sumo 
    res = kingArmy(di-1) + kingArmy(di-2)
    #Guardo en la memoria el resultado
    memoria[di] = res
    #Devuelvo
    return res

n = 10
memoria = [-1 for _ in range(n+1)]
res = kingArmy(n)

#%% Punto 10

def puedeGym(dia, ultAct):
    if diasGym[dia] == True:
        return ultAct != 'GYM'
    else:
        return False
    
def puedeComp(dia, ultAct):
    if diasComp[dia] == True:
        return ultAct != 'COMP'
    else:
        return False
    
    
def vacations(dia, ultAct):
    
    if memo[(dia, ultAct)] != -1:
        return memo[(dia, ultAct)]
    
    if dia == n:
        memo[(dia, ultAct)] = 0
        return 0
    
    sePuedeGym = puedeGym(dia, ultAct)
    sePuedeComp = puedeComp(dia, ultAct)
    
    if sePuedeGym and sePuedeComp:
        res = min(1 + vacations(dia + 1, 'DESC'), vacations(dia + 1, 'GYM'), vacations(dia + 1, 'COMP'))
        memo[(dia, ultAct)] = res
        return res
    
    elif sePuedeGym:
        res = min(1 + vacations(dia + 1, 'DESC'), vacations(dia + 1, 'GYM'))
        memo[(dia, ultAct)] = res
        return res
    
    elif sePuedeComp:
        res = min(1 + vacations(dia + 1, 'DESC'), vacations(dia + 1, 'COMP'))
        memo[(dia, ultAct)] = res
        return res

    else:
        res = 1 + vacations(dia + 1, 'DESC')
        memo[(dia, ultAct)] = res
        return res
    
    
#Ejemplo
n = 4
memo = {(dia, act): -1 for dia in range(n+1) for act in ['DESC', 'GYM', 'COMP']}
dias_gym_disponible = [2, 3]
dias_comp_disponible = [1, 2]
diasGym = [False for _ in range(n)]
diasComp = [False for _ in range(n)]

for dia in dias_gym_disponible:
    diasGym[dia-1] = True

for dia in dias_comp_disponible:
    diasComp[dia-1] = True
    
res = vacations(0, 'DESC')
        
#%% Reconstrucción de la solución

actividades = []
dia = 0
aux = res
while dia < n:
    if aux == 1 + memo[(dia + 1, 'DESC')]:
        actividades.append('DESC')
        aux -= 1
    elif aux == memo[(dia + 1, 'GYM')]:
        actividades.append('GYM')
    else:
        actividades.append('COMP')
        
    dia += 1


#%% función recursiva optipago
def cc(B, j):
    i = len(B)
    
    if j <= 0:
        return (0,0)
    
    if i == 0 and j>0:
        return (float('inf'), float('inf'))
    
    (m, q) = cc(B[:i-1], j)
    (m_prima, q_prima) = cc(B[:i-1], j - B[i-1])
    
    if (m < m_prima + B[i-1]) or ((m == m_prima + B[i-1]) and (q <= q_prima + 1)):
        return (m,q)
    
    else:
        return (m_prima + B[i-1], q_prima + 1)


#%%
c = 14
B = [2,3,5,10,20,20]

res = cc(B, c)

#%% función dinámica optipago
filas = len(B) + 1
columnas = c + 1

# Crear la matriz con (-1, -1) en cada posición
M = [[(-1, -1) for _ in range(columnas)] for _ in range(filas)]

def cc_B (i, j):
    
    if j <= 0:
        return (0,0)
    
    if M[i][j] != (-1, -1):
        return M[i][j]
    
    if i == -1 and j>0:
        return (float('inf'), float('inf'))
    
    (m, q) = cc_B(i-1, j)
    (m_prima, q_prima) = cc_B(i-1, j - B[i])
    
    if (m < m_prima + B[i]) or ((m == m_prima + B[i]) and (q <= q_prima + 1)):
        M[i][j] = (m,q)
        return (m,q)
    
    else:
        M[i][j] = (m_prima + B[i], q_prima + 1)
        return (m_prima + B[i], q_prima + 1)

#%% Ejemplo
res2= cc_B(len(B) - 1, c)

#%% Algoritmo dinámico top-down astrotrade
P = [10,1,11,10,100]
n = len(P)
A = [[None for _ in range(n+1)] for _ in range(n+1)]
def mgn_P(i, c):
    if c < 0 or c > i:
        return float('-inf')

    if A[i][c] is not None:
        return A[i][c]
    
    if i == 0 and c>0:
        A[i][c] = float('-inf')
        return float('-inf')
    
    if i == 0 and c == 0:
        A[i][c] = 0
        return 0
    
    vender = mgn_P(i-1, c+1) + P[i-1]
    comprar = mgn_P(i-1, c-1) - P[i-1]
    no_operar = mgn_P(i-1, c)
    
    maxima_ganancia = max(vender, comprar, no_operar)
    
    A[i][c] = maxima_ganancia
    
    return maxima_ganancia
    

print(mgn_P(n, 0))

#%% Auxiliar para Fire

# Primero usaremos merge_sort para ordenar la lista de artículos
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
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Añadir los restos (solo uno de los dos bucles se ejecutará)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#%%
articulos = [(3,7,4), (2,6,5) ,(3,7,6)]
N = len(articulos)
A = merge_sort(articulos)
D = max(d for (t,d,p) in A)
memo = [[-1 for _ in range(D+1)] for _ in range (N+1)]
def fire(i, tAcum):
    if i == N:
        return 0
    
    if tAcum + A[i][0] >= A[i][1] :
        return float('-inf')

    if memo[i][tAcum] != -1:
        return memo[i][tAcum]
    
    no_salvar_art = fire(i+1, tAcum)
    
    #Solo puedo salvar si tAcum no supera A[i][1], que es el tiempo que tiene el art antes de volverse obsoleto
    salvar_art = float('inf')
    if tAcum + A[i][0] < A[i][1]:    
        salvar_art = fire(i+1, tAcum + A[i][0]) + A[i][2]
    
    valorMaximo = max(no_salvar_art, salvar_art )
    memo[i][tAcum] = valorMaximo
    
    return valorMaximo
    

#%% Ejemplo
print(fire(0, 0))
#%% Reconsruyamos ahora la solución.
articulos_salvados = []
tAcum = 0
for i in range(0, N, 1):
    if memo[i][tAcum] != memo[i+1][tAcum]:
        tAcum += A[i][0]
        articulos_salvados.append(A[i])

#%% Punto 15: cortes económicos
cortes = [2,4,7]
l = 10
C = [i if i in cortes else -1 for i in range(l)]
M = [[-1 for _ in range(l+1)] for _ in range(l+1)]
def costo_minimo(i,j):
    if M[i][j] != -1:
        return M[i][j]
    
    costos = []
    largo_vara = j - i
    for k in range(i+1, j, 1):
        coste_k = 0
        if C[k] != -1:
            coste_k = largo_vara + costo_minimo(i, k) + costo_minimo(k, j)
            costos.append(coste_k)
            
    minimo_corte = 0
    if costos:
        minimo_corte = min(costos) 
    M[i][j] = minimo_corte
    return minimo_corte

print(costo_minimo(0, l))

#%% Punto 15: cortes económicos optimizado
cortes= [2,4,7]
C = [0]
l = 10
for corte in cortes:
    C.append(corte)
C.append(l)
M = [[-1 for _ in range(len(C)+1)] for _ in range(len(C)+1)]
def costo_minimo(i,j):
    if M[i][j] != -1:
        return M[i][j]
    
    izq = C[i]
    der = C[j]
    costos = []
    largo_vara = der - izq
    for k in range(i+1, j, 1):
        coste_k = 0
        coste_k = largo_vara + costo_minimo(i, k) + costo_minimo(k, j)
        costos.append(coste_k)
            
    minimo_corte = 0
    if costos:
        minimo_corte = min(costos) 
    M[i][j] = minimo_corte
    return minimo_corte

print(costo_minimo(0, len(C)-1))

#%% Punto 15: cortes económicos bottom up
cortes= [2,4,7]
l = 10
M = [[0 for _ in range(len(C)+1)] for _ in range(len(C)+1)]
def costo_minimo(l, cortes):
    C = [0]
    l = 10
    for corte in cortes:
        C.append(corte)
    C.append(l)
    for d in range(2, len(C)+1, 1):
        for i in range(0, len(C)-1-d + 1):
            j = i + d
            M[i][j] = float('inf')
            costos = []
            for k in range(i+1,j,1):
                coste_k = C[j] - C[i] + M[i][k] + M[k][j]
                costos.append(coste_k)
            
            if costos:
                M[i][j] = min(costos)
            else:
                M[i][j] = 0

    return M[0][len(C) - 1]

print(costo_minimo(l, cortes))



#%% Punto 16: Travesía Vital
m = 3
n = 3
M = [[float('inf') for _ in range(n)] for _ in range(m)]
A = [[-2, -3, 3], [-5,-10, 1], [10, 30, -5]]
def tv3(i,j):
    
    #Caso información ya guardada
    if M[i][j] != float('inf'):
        return M[i][j]
    
    #Caso base: llegué al final del terreno
    if i == m-1 and j == n-1:
        celda = A[i][j]
        if celda >=0: #Si es positivo, con haber llegado con 1 de vida me alcanza
            return 1
        
        else: #Si es negativo, significa que debo haber llegado con uno más que el valor absoluto de mi celda
            return abs(celda) + 1
        
        
    #Vamos con casos recursivos
    
    mvn = 0
    celda_actual = A[i][j]
    esPocion = (A[i][j] >= 0)
    izq_der_disponibles = (i < m-1 and j < n-1)
    
    if izq_der_disponibles:
        vida_necesaria_a_posteriori = min(tv3(i+1, j), tv3(i, j+1))
        #Tengo dos casos: estoy sobre una poción o sobre veneno
        #Si tengo pocion, y esta basta para soportar el resto del camino, entonces simplemente debo haber llegado con 1 de vida a ella.
        #Si tengo pocion y no me basta, debo de haber entrado con más vida, para poder, junto a la poción, soportar el veneno más tarde
        #Si tengo veneno, debo adicionarle a mi vida necesaria al entrar el valor absoluto del veneno
        #Luego:
        mvn = max(vida_necesaria_a_posteriori - celda_actual, 1)
    #Los casos en los que solo puedo moverme en una dirección son análogos, salvo que está determinado "cuál es mi futuro" (bajar o derecha)
    elif i == m-1:
        vida_necesaria_a_posteriori = tv3(i,j+1)
        mvn = max(vida_necesaria_a_posteriori - celda_actual, 1)
    elif j == n-1:
        vida_necesaria_a_posteriori = tv3(i+1,j)
        mvn = max(vida_necesaria_a_posteriori - celda_actual, 1)
    
    #Guardo valor calculado en mi estructura de memoizacion
    M[i][j] = mvn
    
    return mvn        
    

print(tv3(0,0))



#%% Punto 16: Travesía Vital bottom up
m = 3
n = 3
minimo = min(m,n) 
M = []
M = [float('inf')for _ in range(minimo)]
A = [[-2, -3, 3], [-5,-10, 1], [10, 30, -5]]

def tvBU(A):
    
    m = len(A)
    n = len(A[0])
    mvn = 0
    if m>=n:
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                celda_actual = A[i][j]
                if i == m-1 and j==n-1:
                    mvn = max(-celda_actual + 1, 1)
                    M[j] = mvn
                elif i == m-1:
                    mvn = max(M[j+1] - A[i][j], 1)
                    M[j] = mvn
                elif j == n-1:
                    mvn = max(M[j] - A[i][j], 1)
                    M[j] = mvn
                else:
                    v = min(M[j+1], M[j])
                    mvn = max(v - A[i][j], 1)
                    M[j] = mvn 
    else:
        for j in range(n-1, -1, -1):
            for i in range(m-1, -1, -1):
                celda_actual = A[i][j]
                if i == m-1 and j==n-1:
                    mvn = max(-celda_actual + 1, 1)
                    M[i] = mvn
                elif i == m-1:
                    mvn = max(M[i] - A[i][j], 1)
                    M[i] = mvn
                elif j == n-1:
                    mvn = max(M[i+1] - A[i][j], 1)
                    M[i] = mvn
                else:
                    v = min(M[i], M[i+1])
                    mvn = max(v - A[i][j], 1)
                    M[i] = mvn 
    
    return M[0]
    

test1 = [[1, -3, 3], [0, -2, 0], [-3, -3, -3]]
test2 = [[-5, 2], [1, -1], [-10, -2], [2, -3]]
test3 = [[-2, -5, 10, -1], [10, -1, -5, -2]]

print(f"Test Cuadrado (Esperado 3): {tvBU(test1)}")
print(f"Test Alto (Esperado 10): {tvBU(test2)}")
print(f"Test Ancho (Esperado 3): {tvBU(test3)}")

#%% Punto 17: PilaCauta topdown

N = 5
w= [19,7,5,6,1]
s = [15,13,7,8,2]
cM = max(s)
M = [[float('inf') for _ in range(cM+1)] for _ in range (N+1)]
def pc(i, c):
    
    #Caso info ya guardada
    if M[i][c] != float('inf'):
        return M[i][c]
    
    #Caso todas las cajas ya revisadas
    if i == N:
        return 0
    
    #Caso recursivo
    
    if c == 0: #Caso no se agregó ninguna caja a la pila
        M[i][c] = 1 + pc(i+1, s[i]) + pc(i+1, 0)
        return M[i][c]
    elif c - w[i] <= 0: #caso pila no soporta caja 
        M[i][c] = pc(i+1, c)
        return M[i][c]
    else: #caso pila soporta caja
        M[i][c] = 1 + pc(i+1, min(c - w[i], s[i])) + pc(i+1, c)
        return M[i][c]

print(pc(0, 0))


#%% Punto 17: PilaCauta bottom up
w= [19,7,5,6,1]
s = [15,13,7,8,2]

def pc(N):
    M = {}
    
    for i in range(N):
        dict_aux = M.copy()
        if s[i] in dict_aux:    
            dict_aux[s[i]] += 1
        else:
            dict_aux[s[i]] = 1
        for (soporte, cant_formas) in M.items():
            if soporte - w[i] >= 0:
                soporte_minimo = min(soporte - w[i], s[i])
                if soporte_minimo in dict_aux:
                    dict_aux[soporte_minimo] += cant_formas
                else:
                    dict_aux[soporte_minimo] = cant_formas
        M = dict_aux.copy()
        
    res = 0
    for clave in M:
        res += M[clave]
        
    return res

print(pc(5))

#%% Punto 18: OperacionesSeq
#Función que guarda True/False
v = [3,1,5,2,1]
w = 400
M = [[None for _ in range(w+1)] for _ in range(len(v))]

def os(i, w_prima):
    
    if w_prima < 0 or (i == 0 and w_prima != v[0]):
        return False
    
    if i == 0 and w_prima == v[0]:
        return True
    
    if M[i][w_prima] != None:
        return M[i][w_prima]
    
    res = False
    es_natural_la_resta = (w_prima - v[i] >= 0)
    es_divisible = (w_prima % v[i] == 0)
    raiz_cand = round(w_prima**(1/v[i])) 
    es_natural_la_raiz = (raiz_cand**v[i] == w_prima)
    
    if es_natural_la_resta:
        res = os(i-1, w_prima - v[i])
    if es_divisible:
        res = res or os(i-1, w_prima // v[i])
    if es_natural_la_raiz:
        res = res or os(i-1, raiz_cand)
    
    M[i][w_prima] = res
    
    return res

print(os(len(v) - 1, 400))
                
#%% Punto 18: OperacionesSeq
#Función que guarda símbolo
v = [3,1,5,2,1]
w = 400
M = [[None for _ in range(w+1)] for _ in range(len(v))]

def os(i, w_prima):
    
    if w_prima < 0 or (i == 0 and w_prima != v[0]):
        return False
    
    if M[i][w_prima] != None:
        return M[i][w_prima] != 'nada'
    
    if i == 0 and w_prima == v[0]:
        M[i][w_prima] = True
        return True
    
    res_general = False
    simbolo_alcanzado = 'nada'
    es_natural_la_resta = (w_prima - v[i] >= 0)
    es_divisible = (w_prima % v[i] == 0)
    raiz_cand = round(w_prima**(1/v[i])) 
    es_natural_la_raiz = (raiz_cand**v[i] == w_prima)
    
    if es_natural_la_resta:
        res_resta = os(i-1, w_prima - v[i])
        res_general = res_resta
        if res_resta is True:
            simbolo_alcanzado = '+'
    if es_divisible and not(res_general):
        res_division = os(i-1, w_prima // v[i])
        res_general = res_general or res_division
        if res_division is True:
            simbolo_alcanzado = 'x'
    if es_natural_la_raiz and not(res_general):
        res_raiz = os(i-1, raiz_cand)
        res_general = res_general or res_raiz
        if res_raiz is True:
            simbolo_alcanzado = '↑'
    
    M[i][w_prima] = simbolo_alcanzado
    
    return res_general

existe_sol = os(len(v) - 1, 400)
print(existe_sol)
#Reconstruyamos la solución
if existe_sol:
    res_reverso = []
    res_real = []
    w_prima = w
    for i in range(len(v) - 1, 0, -1):
        res_reverso.append(M[i][w_prima])
        simbolo = M[i][w_prima]
        if simbolo == '+':
            w_prima = w_prima - v[i]
        elif simbolo == 'x':
            w_prima = w_prima // v[i]
        else:
            w_prima = round(w_prima**(1/v[i])) 

    for j in range(len(res_reverso) - 1, -1, -1):
        res_real.append(res_reverso[j])
    
    print(res_real)


#%% Punto 18: OperacionesSeq algoritmo bottom up

#Función que guarda símbolo
v = [3,1,5,2,1]
w = 400

def os(v, w):
    N = len(v)
    M = {}
    M[0] = {v[0]: (0,0)}
    for i in range(1, N):
        M_aux = {}
        for (clave, (valor_anterior, operacion_anterior)) in M[i-1].items():
            suma = clave + v[i]
            multiplicacion = clave*v[i]
            potencia = clave**v[i]
            if suma <= w:
                M_aux[suma] = (clave, '+') 
            if multiplicacion <=w:
                M_aux[multiplicacion] = (clave, 'x')
            if potencia <= w:
                M_aux[potencia] = (clave, '↑')
        
        M[i] = M_aux
    
    return (w in M[N-1], M) 
        

existe_sol, M = os(v,w)

if existe_sol:
    res_reverso = []
    res_real = []
    w_prima = w
    for i in range(len(v) - 1, 0, -1):
        simbolo = M[i][w_prima][1]
        w_prima = M[i][w_prima][0]
        res_reverso.append(simbolo)
    

    for j in range(len(res_reverso) - 1, -1, -1):
        res_real.append(res_reverso[j])
    
    print(res_real)














