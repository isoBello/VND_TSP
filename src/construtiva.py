#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

# Heurística que constrói a solução inicial utilizada pelo VND. Baseada na heurística do vizinho mais próximo
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