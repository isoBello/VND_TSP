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


def construtor(u, v, w, k, caminho, distancias, custo):
    novo_caminho = []
    i, aux = 0, len(caminho) - 1
    
    while i < aux:
        if caminho[i] == u:
            try:
                novo_caminho = swap(u,v,w,k,novo_caminho)
                i = caminho.index(caminho[i]) + 4
            except IndexError:
                novo_caminho = swap(u,v,w,k,novo_caminho)
                break
        else:
            novo_caminho.append(caminho[i])
            i += 1

    novo_caminho.append(caminho[0])
    dist_total = distanciagetter(novo_caminho, distancias)
    return (dist_total, novo_caminho)

def swap(u,v,w,k,novo_caminho):
    novo_caminho.append(u)
    novo_caminho.append(w)
    novo_caminho.append(v)
    novo_caminho.append(k)
    return novo_caminho

def distanciagetter(novo_caminho, distancias):
    dist = 0
    for i in range(len(novo_caminho) - 1):
        for j in distancias.get(novo_caminho[i]):
            if j[0] == novo_caminho[i + 1]:
                dist += j[1]
                break
    return dist