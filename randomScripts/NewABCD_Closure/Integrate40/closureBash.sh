#!/bin/bash

years=("18" "17" "16" "16APV" "RunII")

cases=("Default" "CRTT" "CRDY" "EMu")

types=("total_background" "total_data")

for year in "${years[@]}"; do
    for case in "${cases[@]}"; do
        for type in "${types[@]}"; do
            command="python closurePlotter_Integrate40.py /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/${case}_2D_${year} ${type} 14 21 220 135 /eos/user/g/gdecastr/SUEPCoffea_dask/CommonClosures_Integrate40/${year}_${case}_${type}"
            echo $command
            $command 
        done
    done
done
