#!/bin/bash

source_dir="../"
target_dir=""

for region in "CRDY" "CRTT" "SR" "EMu"; do
    for year in "18" "17" "16" "16APV"; do
        rm -rf "${region}_2D_${year}"
        mkdir "${region}_2D_${year}"
        for data_type in "total_data" "total_background"; do
            if [ "$region" == "SR" ]; then
                source_file="${source_dir}${year}_Default_${data_type}.root"
                target_file="${region}_2D_${year}/${data_type}.root"
            else
                source_file="${source_dir}${year}_${region}_${data_type}.root"
                target_file="${region}_2D_${year}/${data_type}.root"
            fi
            cp "$source_file" "${target_dir}$target_file"
            echo "$source_file" "${target_dir}$target_file"
        done
    done
done
