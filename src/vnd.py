#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from construtiva import heuristica_construtiva
from neighborhood import vizinhança 

def VND():
    x = heuristica_construtiva()
    vizinhanças = 4
    melhor_solucao = x
    aux = 0

    while aux < vizinhanças:
        primeiro_aprimorante = vizinhança(aux, x)
        if fitness(primeiro_aprimorante) < fitness(x):
            melhor_solucao = primeiro_aprimorante
            aux = 0
        else:
            aux += 1
    return melhor_solucao

def fitness(s):
    return s[0]