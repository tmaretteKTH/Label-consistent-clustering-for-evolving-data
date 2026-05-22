#!/bin/bash
declare -a historicals=("Resilient")
#declare -a datasets=("Uber" "Twitter" "OnlineRetail" "Electricity")
#Uber and Twitter need to be installed manually.
declare -a datasets=("OnlineRetail" "Electricity")
declare -a ks=(30)
mkdir results/setup2
for k in "${ks[@]}"
do
        for dataset in "${datasets[@]}"
        do
		mkdir results/setup2/$dataset
                for historical in "${historicals[@]}"
                do
                        python3 src/setup2.py $dataset $historical $k &
                done
        done
done
python3 src/plotsForSetup2.py
