#!/bin/bash

output_path="$1"
cutVarTrack1="$2"
cutVarTrack2="$3"
cutVarJet1="$4"
cutVarJet2="$5"
UpperTrackBin="$6"

years=("18" "17" "16" "16APV" "RunII")
cases=("Default" "CRTT" "CRDY" "EMu")
types=("total_background" "total_data")

for year in "${years[@]}"; do
    for case in "${cases[@]}"; do
        for type in "${types[@]}"; do
            command="python closurePlotter.py /eos/user/g/gdecastr/SUEPCoffea_dask/Plots/${case}_2D_${year} ${type} ${cutVarTrack1} ${cutVarTrack2} ${cutVarJet1} ${cutVarJet2} ${output_path}/${year}_${case}_${type} ${UpperTrackBin}" 
            echo "$command"
            $command
        done
    done
done