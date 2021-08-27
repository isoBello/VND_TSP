#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

import csv
import sys
import json 

def grafo(vertices, distancias, output):
    distancias[0].append(vertices)
    with open(output, 'w') as file:
        for key, value in distancias.items(): 
            file.write('%s:%s\n' % (key, value))


def Main(iteracao, algoritmo, n_arq, solucao):
    filename = "./saida.csv"
    with open(filename, 'a') as output:
        csvwriter = csv.writer(output)
        
        rows = [[iteracao, algoritmo, n_arq, round(solucao, 4)]]
        csvwriter.writerows(rows)