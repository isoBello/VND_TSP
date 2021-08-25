#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

# Heurística que constrói a solução inicial utilizada pelo VND. 
# Baseada na heurística do vizinho mais próximo
import heapq
from numpy import random

def heuristica_construtiva(vertices, distancias):
    visita = [False] * vertices
    u = random.randint(1, vertices)
    visita[u] = True

    pilha = [(0, u)]
    dist_total = 0
    caminho = []

    while len(caminho) <= vertices and pilha:
        distancia, u = heapq.heappop(pilha)

        while visita[u] and pilha:
            distancia, u = heapq.heappop(pilha)
        
        visita[u] = True
        pilha.clear()

        if u not in caminho:
            caminho.append(u)
            dist_total += distancia
        
        for v in distancias.get(u):
            if not visita[v[0]]:
                heapq.heappush(pilha, (v[1], v[0]))

    for v in distancias.get(caminho[0]):
        if v[0] == caminho[-1]:
            dist_total += v[1]
            caminho.append(caminho[0])
            break
    return (dist_total, caminho) 


def construtor(u, v, caminho, distancias, w=None, k=None, tipo=False):
    if (w and k) is not None:
        _x, _y = caminho.index(u), caminho.index(w)
        x, y = caminho.index(v), caminho.index(k)

        if tipo:
            caminho[_x], caminho[_y] = caminho[_y], caminho[_x]
            caminho[x], caminho[y] = caminho[y], caminho[x]
        else:
            caminho[x], caminho[_y] = caminho[_y], caminho[x]
    else:
        _x, _y = caminho.index(u), caminho.index(v)
        caminho[_x], caminho[_y] = caminho[_y], caminho[_x]

    caminho[-1] = caminho[0]
    dist_total = distanciagetter(caminho, distancias)
    return (dist_total, caminho)


def distanciagetter(caminho, distancias):
    dist = 0
    for i in range(len(caminho) - 1):
        for j in distancias.get(caminho[i]):
            if j[0] == caminho[i + 1]:
                dist += j[1]
                break
    return dist
