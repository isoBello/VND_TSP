#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

import sys
from .distancias import calculadora
from .vnd import Main

def Grafo():
    header = []
    with open(sys.argv[1]) as f:
        for line in iter(lambda: f.readline().rstrip(), 'NODE_COORD_SECTION'):
            header.append(line)
        qtd_vertices, tipo_dist = infogetter(header)
           
        line = next(f)
        while 'EOF' not in line:
            v, x, y = valuesgetter(line)
            coordenadas[v] = (x, y)
            line = next(f)

    return qtd_vertices + 1, coordenadas, tipo_dist
           

def infogetter(head):
    for info in head:
        if 'DIMENSION' in info:
            qtd_vertices = int(info.split(": ")[1])
        elif 'EDGE_WEIGHT_TYPE' in info:
            tipo_dist = info.split(": ")[1]
    return qtd_vertices, tipo_dist


def valuesgetter(line):
    values = line.split(" ")
    try:
        v = int(values[0])
        x = float(values[1])
        y = float(values[2])
        return v, x, y
    except ValueError:
        pass

if __name__ == "__main__":
    vertices, coordenadas, tipo_dist = Grafo()

    if "GEO" in tipo_dist:
        distancias = calculadora(vertices, coordenadas, 0)
    else:
        distancias = calculadora(vertices, coordenadas, 1)

    solucao = Main(vertices, distancias)