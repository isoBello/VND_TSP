#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from construtiva import heuristica_construtiva
from neighborhood import neighborhood

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


def MainVND(vertices, distancias):
    s_inicial = heuristica_construtiva(vertices, distancias)
    return VND(s_inicial, distancias)