#!/VND_TSP/virtual/bin python3.6
# -*- coding: utf-8 -*-

import glob
import threading
from entrada import main
from vnd import main_vnd
from vns import main_vns 

arquivo = 1

def exec_vnd(file, target, n_arq):
    for i in range(1, target):
        main_vnd(file, i, 1, n_arq)

def exec_vns(file, target, n_arq):
    for i in range(1, target):
        main_vns(file, i, 1, n_arq)


def thread():
    grupo_1 = glob.glob("./Grupo 1/*.tsp")
    grupo_2 = glob.glob("./Grupo 2/*.tsp")
    grupo_3 = glob.glob("./Grupo 3/*.tsp")

    target = 16
    global arquivo
    for file in grupo_1:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_1 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_2 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_1.start()
        thread_2.start()
        arquivo += 1

    arquivo = 0
    for file in grupo_1:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_3 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_4 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_3.start()
        thread_4.start()
        arquivo += 1
    
    print("End, iniciating group 2")

    arquivo = len(grupo_1)
    for file in grupo_2:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_1 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_2 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_1.start()
        thread_2.start()
        arquivo += 1
    
    arquivo = len(grupo_1)
    for file in grupo_2:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_3 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_4 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_3.start()
        thread_4.start()
        arquivo += 1
    
    print("End, iniciating group 3")
    
    arquivo = len(grupo_2)
    for file in grupo_3:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_1 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_2 = threading.Thread(target=exec_vnd(output, target, arquivo))
        thread_1.start()
        thread_2.start()
        arquivo += 1
    
    arquivo = len(grupo_2)
    for file in grupo_3:
        arq = file.split("/")[2].replace(".tsp", "")
        output = "./Grafos/grafo" + arq + ".dat"
        main(file, output)
        thread_3 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_4 = threading.Thread(target=exec_vns(output, target, arquivo))
        thread_3.start()
        thread_4.start()
        arquivo += 1

if __name__ == "__main__":
    thread()


