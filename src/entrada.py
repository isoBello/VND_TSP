#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
import re
from distancias import calculadora
from saida import grafo


def Grafo(filename):
    header = []
    coordenadas = {}

    with open(filename) as f:
        for line in iter(lambda: f.readline().rstrip(), 'NODE_COORD_SECTION'):
            header.append(line)
        qtd_vertices, tipo_dist = infogetter(header)
           
        line = next(f)
        while True:
            try:
                v, x, y = valuesgetter(line)
                coordenadas[v] = (x, y)
                line = next(f)
            except (TypeError, IndexError):
                break
        return qtd_vertices + 1, coordenadas, tipo_dist
           

def infogetter(head):
    for info in head:
        if 'DIMENSION' in info:
            qtd_vertices = int(info.split(": ")[1])
        elif 'EDGE_WEIGHT_TYPE' in info:
            tipo_dist = info.split(": ")[1]
    return qtd_vertices, tipo_dist


def valuesgetter(line):
    regex = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", line)
    return int(regex[0]), float(regex[1]), float(regex[2])

def main(filename, output):
    vertices, coordenadas, tipo_dist = Grafo(filename)

    if "GEO" in tipo_dist:
        distancias = calculadora(vertices, coordenadas, 0)
    else:
        distancias = calculadora(vertices, coordenadas, 1)

    grafo(vertices, distancias, output)