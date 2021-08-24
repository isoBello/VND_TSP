#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-


# s é a solução inicial (partida) de cada vizinhança

def vizinhança(operador, s):
    if operador == 0:
        return opt_2(s)
    elif operador == 1:
        return opt_or(s)
    elif operador == 2:
        return opt_3(s)
    else:
        return swap(s)
#def opt_2(s):

''' def opt_or(s):
def opt_3(s):
def swap(s): '''
