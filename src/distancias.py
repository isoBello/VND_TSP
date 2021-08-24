#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-
from collections import defaultdict
from math import sqrt, pi, sin, cos, acos

def calculadora(vertices, coordenadas, tipo):
    distancias = defaultdict(list)

    for i in range(1, vertices):
        _x, _y = coordenadas.get(i)[0], coordenadas.get(i)[1]
        for k, v in coordenadas.items():
            if k == i:
                pass
            
            x, y = v[0], v[1]
            distancias[i].append((k, calcular_distancia(_x,_y, x, y, tipo)))
    return distancias

def calcular_distancia(_x, _y, x, y, tipo):
    lat_a = _x * pi / 180
    lat_b = x * pi / 180
    long_a = _y * pi / 180
    long_b = y * pi / 180
    
    
    if tipo == 0:
        geo(long_a - long_b, lat_a, lat_b, long_a, long_b)
    else:
        euc(_x - x, _y - y)


def geo(y, lat_a, lat_b, long_a, long_b):
    raio = 6372.795477598
    distancia = raio * acos(sin(lat_a) * sin(lat_b) + cos(lat_a) * cos(lat_b) * cos(y)) 
    return distancia

def euc(x, y):
    distancia = sqrt(pow(x, 2) + pow(y, 2))
    return distancia