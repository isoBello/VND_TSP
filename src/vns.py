#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from construtiva import heuristica_construtiva
from neighborhood import neighborhood
from vnd import VND
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

def VNS_VND(s_inicial, distancias):
    max_iteracoes, r = 0, 4
    s = s_inicial

    while max_iteracoes < 30:
        k = 0
        while k < r:
            s_linha = neighborhood(k, s, distancias)
            s_estrela = VND(s_linha, distancias)
            if fitness(s_estrela) < fitness(s_linha):
                s = s_estrela
                k = 1
            else:
                k += 1
        max_iteracoes += 1

def fitness(s):
    return s[0]


if __name__ == "__main__":
    vertices, distancias = Grafo()
    s_inicial = heuristica_construtiva(vertices, distancias)
    Main(VNS_VND(s_inicial, distancias))