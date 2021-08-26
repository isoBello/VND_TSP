#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from construtiva import heuristica_construtiva
from neighborhood import neighborhood
from saida import Main
import sys
import ast 

def Grafo():
    distancias = {}

    with open(sys.argv[1]) as file:
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


if __name__ == "__main__":
    vertices, distancias = Grafo()
    s_inicial = heuristica_construtiva(vertices, distancias)
    Main(VND(s_inicial, distancias))