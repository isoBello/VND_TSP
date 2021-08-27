#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from construtiva import heuristica_construtiva
from neighborhood import neighborhood
from saida import Main
import ast 

def Grafo(filename):
    distancias = {}

    with open(filename) as file:
        for line in file:
            key, value = line.split(":")
            distancias[int(key)] = ast.literal_eval(value)
    return distancias.get(0)[0], distancias

def VND(s_inicial, distancias):
    r = 4
    s = s_inicial
    k = 0

    while k < r:
        s_linha = neighborhood(k, s, distancias)
        if fitness(s_linha) < fitness(s):
            s = s_linha
            k = 0
        else:
            k += 1
    return s

def fitness(s):
    return s[0]


def main_vnd(filename, iteracao, algoritmo, n_arq):
    vertices, distancias = Grafo(filename)
    s_inicial = heuristica_construtiva(vertices, distancias)
    solucao = VND(s_inicial, distancias)
    Main(iteracao, algoritmo, n_arq, solucao[0])