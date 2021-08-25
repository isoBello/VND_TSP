#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-


# s é a solução inicial (partida) de cada vizinhança

from collections import defaultdict
from construtiva import construtor
from numpy import random
from copy import deepcopy

def vizinhança(operador, s, distancias):
    arestas = arestasgetter(s[1])
    if operador == 0:
        return opt_2(arestas, distancias, caminho=s[1])
    elif operador == 1:
        #t = random.randint(0, 1) 
        t = 1
        if t == 0:
            return or_opt1(distancias, caminho=s[1])
        return or_opt2(distancias, caminho=s[1], custo=s[0])

    '''elif operador == 2:
        return opt_3(arestas, caminho=s[1], custo_inicial=s[0])
    else:
        return swap(arestas, caminho=s[1], custo_inicial=s[0]) '''
    

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
    return melhores

    
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
    return melhores 


def or_opt2(distancias, caminho, custo):
    espaco_solucoes = []
    melhores = []

    for i in range(len(caminho) - 4):
        for j in range(i + 2, len(caminho) - 1):
            u, v, w, k = caminho[i], caminho[i + 1], caminho[j], caminho[j + 1]
            h_linha = construtor(u, v, deepcopy(caminho), distancias, w, k, True)
            espaco_solucoes.append(h_linha)
        melhores.append(encontra_melhor_vizinho(espaco_solucoes))
        espaco_solucoes.clear()
    return melhores 



def encontra_melhor_vizinho(N):
    N.sort(key=lambda y: y[0])
    return N[0]

def arestasgetter(vertices):
    arestas = []
    arestas.append((vertices[0], vertices[1]))
    
    for i in range(2, len(vertices) - 1, 2):
        arestas.append((vertices[i - 1], vertices[i]))
        arestas.append((vertices[i], vertices[i + 1]))

    arestas.append((vertices[-2], vertices[0]))
    return arestas
