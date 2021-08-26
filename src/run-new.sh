#!/usr/bin/env fish

source "../virtual/bin/activate.fish"

set arquivo 1
set algoritmo 1
set grafos "../Grafos/"

for entry in "../Data/"/*.tsp
    time -v python3 entrada.py "$entry" "$grafos""grafo$arquivo.dat"
	for count in (seq 1 30)
        time -v python3 vnd.py "$grafos""grafo$arquivo.dat" "$count" "$arquivo" "$algoritmo" "saida.csv"
    end
    set algoritmo (math $algoritmo + 1)
    for count in (seq 1 30)
        time -v python3 vns.py "$grafos""grafo$arquivo.dat" "$count" "$arquivo" "$algoritmo" "saida.csv"
    end
    set arquivo (math $arquivo + 1)
end
deactivate