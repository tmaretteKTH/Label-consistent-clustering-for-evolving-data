#!/bin/bash
declare -a historicals=("Resilient")
declare -a ks=(10 20 50)

for k in "${ks[@]}"
do  
        for historical in "${historicals[@]}"
        do
                python3 src/setup3.py $historical $k
        done
done
python3 src/plotsForSetup3.py
