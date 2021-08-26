#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
# s é a solução inicial (partida) de cada vizinhança
from collections import defaultdict
from construtiva import construtor, reversaogetter, distanciagetter
from numpy import random
from copy import deepcopy

def neighborhood(operador, s, distancias):
    if operador == 0:
        arestas = arestasgetter(s[1])
        return opt_2(arestas, distancias, caminho=s[1])
    elif operador == 1:
        return or_opt1(distancias, caminho=s[1])
    elif operador == 2:
        return or_opt2(distancias, caminho=s[1])
    else:
        return opt_3(distancias, caminho=s[1])
    

def opt_2(arestas, distancias, caminho):
    espaco_solucoes = []
    melhores = []
    visitadas = []

    for i in range(len(arestas) - 1):
        for j in range(len(arestas)):
            u, v, w, k = arestas[i][0], arestas[i][1], arestas[j][0], arestas[j][1]
            if u == k or v == w or arestas[i] == arestas[j] or ((arestas[j], arestas[i])) in visitadas:
                continue
            visitadas.append((arestas[i], arestas[j]))
            h_linha = construtor(u, v, deepcopy(caminho), distancias, w, k)
            espaco_solucoes.append(h_linha)

        melhores.append(encontra_melhor_vizinho(espaco_solucoes))
        espaco_solucoes.clear()

    try:
        melhores.sort(key = lambda x: x[0])
    except TypeError:
        pass
    return melhores[0]

    
def or_opt1(distancias, caminho):
    espaco_solucoes = []
    melhores = []

    for i in range(len(caminho) - 2):
        for j in range(i + 1, len(caminho) - 1):
            u, v = caminho[i], caminho[j]
            h_linha = construtor(u, v, deepcopy(caminho), distancias)
            espaco_solucoes.append(h_linha)
        melhores.append(encontra_melhor_vizinho(espaco_solucoes))
        espaco_solucoes.clear()

    try:
        melhores.sort(key = lambda x: x[0])
    except TypeError:
        pass
    return melhores[0]


def or_opt2(distancias, caminho):
    espaco_solucoes = []
    melhores = []

    for i in range(len(caminho) - 4):
        for j in range(i + 2, len(caminho) - 1):
            u, v, w, k = caminho[i], caminho[i + 1], caminho[j], caminho[j + 1]
            h_linha = construtor(u, v, deepcopy(caminho), distancias, w, k, True)
            espaco_solucoes.append(h_linha)
        melhores.append(encontra_melhor_vizinho(espaco_solucoes))
        espaco_solucoes.clear()
    
    try:
        melhores.sort(key = lambda x: x[0])
    except TypeError:
        pass
    return melhores[0]

def opt_3(distancias, caminho):
    while True:
        delta = 0 
        for(a, b, c) in segmentos(len(caminho)):
            delta += reversaogetter(caminho, a, b, c, distancias)
        if delta >= 0:
            break
    return (distanciagetter(caminho, distancias), caminho)

def segmentos(N):
    return ((i, j, k)
        for i in range(N)
        for j in range(i + 2, N)
        for k in range(j + 2, N + (i > 0)))

def encontra_melhor_vizinho(N):
    try:
        N.sort(key=lambda y: y[0])
        return N[0][0], N[0][1]
    except IndexError:
        pass

def arestasgetter(vertices):
    arestas = []
    arestas.append((vertices[0], vertices[1]))
    
    for i in range(2, len(vertices) - 1, 2):
        arestas.append((vertices[i - 1], vertices[i]))
        arestas.append((vertices[i], vertices[i + 1]))

    arestas.append((vertices[-2], vertices[0]))
    return arestas
