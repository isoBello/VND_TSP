#!/usr/bin/env fish

source "../virtual/bin/activate.fish"

set dirin "../Data/ulysses16.tsp"

python3 entrada.py "$dirin" 

deactivate