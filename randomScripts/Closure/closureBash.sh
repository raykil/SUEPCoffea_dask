#!/bin/bash

output_path="$1"
lower_bin="$2"
upper_bin="$3"

years=("18" "17" "16" "16APV" "RunII")
cases=("Default" "CRTT" "CRDY" "EMu")
types=("total_background" "total_data")

for year in "${years[@]}"; do
    for case in "${cases[@]}"; do
        for type in "${types[@]}"; do
            command="python closurePlotter.py /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/${case}_2D_${year} ${type} ${output_path}/${year}_${case}_${type} ${lower_bin} ${upper_bin}" 
            echo "$command"
            $command
        done
    done
done