#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-


# s é a solução inicial (partida) de cada vizinhança

from collections import defaultdict


def vizinhança(operador, s):
    arestas = arestasgetter(s[1])

    if operador == 0:
        return opt_2(arestas, caminho=s[1], custo_inicial=s[0])
    elif operador == 1:
        return opt_or(arestas, caminho=s[1], custo_inicial=s[0])
    elif operador == 2:
        return opt_3(arestas, caminho=s[1], custo_inicial=s[0])
    else:
        return swap(arestas, caminho=s[1], custo_inicial=s[0])
    

def opt_2(arestas, caminho, custo_inicial):
    caminho = caminho
def opt_or(arestas, caminho, custo_inicial):
    caminho = caminho
def opt_3(arestas, caminho, custo_inicial):
    caminho = caminho
def swap(arestas, caminho, custo_inicial): 
    caminho = caminho


def arestasgetter(vertices):
    arestas = defaultdict(list)
    arestas[vertices[0]].append(vertices[1])
    arestas[vertices[0]].append(vertices[-2])
    for v in range(1, len(vertices) - 1):
        arestas[vertices[v]].append(vertices[v - 1])
        arestas[vertices[v]].append(vertices[v + 1])
    return arestas
