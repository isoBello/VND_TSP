#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

import csv
import sys
import json 

def grafo(vertices, distancias):
    distancias[0].append(vertices)
    with open(sys.argv[2], 'w') as file:
        for key, value in distancias.items(): 
            file.write('%s:%s\n' % (key, value))


def Main(solucao):
    filename = sys.argv[5] 
    with open(filename, 'w') as output:
        csvwriter = csv.writer(output)
        
        iteracao = int(sys.argv[2])
        instancia = int(sys.argv[3])
        algoritmo = int(sys.argv[4])

        rows = [[iteracao, algoritmo, instancia, solucao[0], solucao[1]]]

        print(
        "RESULTADO: " + solucao[0] + " " + solucao[1] + "\n")
        csvwriter.writerows(rows)