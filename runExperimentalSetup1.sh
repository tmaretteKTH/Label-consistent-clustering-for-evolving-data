#!/bin/bash
declare -a historicals=("Carv" "Resilient" "FFT")
# declare -a datasets=("Uber" "Twitter" "Abalone" "OnlineRetail" "Electricity")
# Uber and Twitter need to be installed manually.
declare -a datasets=("Electricity" "OnlineRetail" "Abalone")
declare -a ks=(10 20 50)
for k in "${ks[@]}"
do
        for dataset in "${datasets[@]}"
        do
                for historical in "${historicals[@]}"
                do      
                echo $dataset $historical $k
                        python3 src/setup1.py $dataset $historical $k
                done
        done
done
python3 src/plotsForSetup1.py

